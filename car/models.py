from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User
# Create your models here.


class CarModel(models.Model):
    car_img = models.ImageField(
        upload_to='car/media/uploads/', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    brand_name = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    purchased = models.ManyToManyField(
        User, related_name='purchased', blank=True)

    def __str__(self):
        return self.name
