from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Szafka(models.Model):
    nazwa       = models.CharField (max_length=300)
    szerokosc   = models.IntegerField(default=False)
    wysokosc    = models.IntegerField(default=False)
    glebokosc   = models.IntegerField(default=False)
    plyta       = models.IntegerField(default=False)
    ilosc_polek = models.IntegerField(default=False)
    wzor_frontu = models.CharField(max_length=300,default=False)
    wzor_sciany = models.CharField(max_length=300,default=False)
