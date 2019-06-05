from django.db import models
from core.models.Contrato import Contrato


class Boleto(models.Model):
    STATUS_CHOICES = [
        ('PG', 'PAGO'),
        ('AB', 'EM ABERTO')
    ]
    contrato = models.ForeignKey(Contrato, on_delete=models.DO_NOTHING)
    parcela = models.IntegerField()
    valor_total = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default="AB")

    class Meta:
        managed = True
        db_table = 'boleto'
