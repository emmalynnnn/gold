from django.db import models

# Create your models here.

class ConversionFactor(models.Model):
    name = models.CharField(max_length=3)
    to_troy_oz = models.FloatField()
    def __str__(self):
        return self.name
