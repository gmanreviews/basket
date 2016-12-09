from django.db import models
from django.conf import settings

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=999,decimal_places=2)
    pdf_location = models.CharField(max_length=200, blank=True)
    audio_location = models.CharField(max_length=200, blank= True)
    paperback = models.BooleanField(default=0)
    pdf = models.BooleanField(default=0)
    audio = models.BooleanField(default=0)
