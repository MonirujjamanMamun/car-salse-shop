from django.shortcuts import render
from car.models import CarModel
from brand.models import BrandModel
from car.forms import CarForm


def home(request, brand_slug=None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        brands = BrandModel.objects.get(slug=brand_slug)
        data = CarModel.objects.filter(brand_name=brands)
    brand = BrandModel.objects.all()
    return render(request, 'home.html', {"data": data, 'brands': brand})
