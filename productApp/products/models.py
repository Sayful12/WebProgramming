from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
  