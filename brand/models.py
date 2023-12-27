from django.db import models

# Create your models here.


class BrandModel(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
