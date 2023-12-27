from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, TemplateView
from car.models import CarModel
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_login')

    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})


class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def user_logout(request):
    messages.success(request, 'Log Out Successful.')
    logout(request)
    return redirect('user_login')


# @method_decorator(login_required, name='dispatch')
class DetailPostView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['profiles'] = comments
        context['profiles_form'] = comment_form
        return context


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(
            request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')

    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': profile_form})


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    model = CarModel
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchased'] = self.request.user.purchased.all()
        return context


@login_required
def purchase_car(request, id):
    car = CarModel.objects.get(pk=id)

    if car.quantity > 0:
        car.quantity -= 1
        car.purchased.add(request.user)
        car.save()
        return redirect('profile')
    return redirect('home')
