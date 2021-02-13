from django.db import models
from PIL import Image

# Create your models here.
class Pharmacy(models.Model):
    # title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # description = models.TextField()
    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price= models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name

class Kipharma(models.Model):
    location = models.CharField(max_length=255)
    medicinename = models.CharField(max_length=255)
    medicinedescription = models.CharField(max_length=255)
    medicineprice = models.CharField(max_length=255)
    def __str__(self):
        return self.location

class Postnews(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    # location =models.CharField(max_length=255)
    image = models.ImageField()
    price =models.CharField(max_length=255)
    description = models.TextField()
    def _str_(self):
        return self.title

# Create your models here.
