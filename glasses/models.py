from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils import timezone

import os

from enum import Enum

class GlassCategory(Enum):
    
    UNDEFINED = "Indéterminé"
    WEDDING = "Mariage"
    BIRTHDAY = "Anniversaire"
    CHRISTMAS = "Noël"
    EASTER = "Pâques"

    @classmethod
    def choices(cls):
        return tuple((literal.name, literal.value) for literal in cls)


class Glass(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    category = models.CharField(max_length=50, null=False, blank=True, choices=GlassCategory.choices(), default=GlassCategory.UNDEFINED)
    amount = models.PositiveIntegerField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0)])
    image = models.ImageField(upload_to='images/', blank=False)
    creation_moment = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name