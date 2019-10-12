from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
import os

from enum import Enum

class GlassCategory(Enum):
    
    UNDEFINED = "Indéterminé"
    WEDDING = "Marriage"
    BIRTHDAY = "Anniversaire"
    CHRISTMAS = "Noël"
    EASTER = "Pâques"

    @classmethod
    def choices(cls):
        return tuple((literal.name, literal.value) for literal in cls)


class Glass(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False, choices=GlassCategory.choices(), default=GlassCategory.UNDEFINED)
    amount = models.PositiveIntegerField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0)])
    image = models.ImageField(upload_to='images/', blank=False)

    def __str__(self):
        return self.name