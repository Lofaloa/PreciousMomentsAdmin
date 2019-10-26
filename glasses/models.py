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
    """ Represents a glass made by the administrator. """
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    category = models.CharField(max_length=50, null=False, blank=True, choices=GlassCategory.choices(), default=GlassCategory.UNDEFINED)
    amount = models.PositiveIntegerField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0)])
    image = models.ImageField(upload_to='images/', blank=False)
    creation_moment = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    """ Represents a company that supplies the administrator. """
    name = models.CharField(max_length=50, null=False, blank=False, unique=False)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    """ Represents a raw material used to craft glasses """
    name = models.CharField(max_length=50, null=False, blank=False, unique=False)
    available_amount = models.PositiveIntegerField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0)])
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    glasses = models.ManyToManyField(Glass)

    def __str__(self):
        return self.name + " (" + "fournis par " + self.supplier.name + ")"

