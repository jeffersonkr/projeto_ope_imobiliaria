from django.db import models
from core.models.Pessoa import Pessoa


class Corretor(models.Model):
    creci = models.CharField(max_length=50)


    class Meta:
        managed = True
        db_table = 'corretor'

