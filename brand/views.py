from django.shortcuts import render
from django.views.generic import CreateView
from .models import BrandModel
from .forms import BrandForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator(login_required, name='dispatch')
class AddBrandView(CreateView):
    model = BrandModel
    form_class = BrandForm
    success_url = reverse_lazy('home')
    template_name = 'add_brand.html'

    def form_valid(self, form):
        return super().form_valid(form)
