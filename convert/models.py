from django.db import models

# Create your models here.

class ConversionFactor(models.Model):
    name = models.CharField(max_length=3)
    to_pounds = models.FloatField()
