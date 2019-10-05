from django.db import models
from django.conf import settings
import os

class Glass(models.Model):
    name = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name