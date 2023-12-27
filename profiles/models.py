from django.db import models
from car.models import CarModel
# Create your models here.


class Comment(models.Model):
    car = models.ForeignKey(
        CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
