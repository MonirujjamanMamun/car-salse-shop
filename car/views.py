from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import CarModel
from .forms import CarForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


@method_decorator(login_required, name='dispatch')
class AddCarView(CreateView):
    model = CarModel
    form_class = CarForm
    template_name = 'add_car.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
