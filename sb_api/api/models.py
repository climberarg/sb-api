from django.db import models

# Create your models here.

class BackScratcher(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    size = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=6, decimal_places=2)
