from django.db import models

class Glass(models.Model):
    name = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name