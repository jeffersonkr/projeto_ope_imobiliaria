from django.db import models
from .Cliente import Cliente
from .Imovel import Imovel
from .Proprietario import Proprietario
from .Corretor import Corretor

class GoogleMaps(models.Model):

    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
 
    class Meta:
        managed = True
        db_table = 'mapa'