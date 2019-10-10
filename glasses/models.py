from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
import os

class Glass(models.Model):
    name = models.CharField(max_length=50, null=False)
    amount = models.PositiveIntegerField(null=False)
    price = models.FloatField(null=False, validators=[MinValueValidator(0.0)])
    image = models.ImageField(upload_to='images/', null=False)

    def __str__(self):
        return self.name