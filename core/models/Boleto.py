from django.db import models
from core.models.Contrato import Contrato


class Boleto(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'boleto'
