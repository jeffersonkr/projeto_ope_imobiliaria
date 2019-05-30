from django.db import models
from .Aluguel import Aluguel
from .Venda import Venda
from .Cliente import Cliente
from .Proprietario import Proprietario



class Boleto(models.Model):
    #id_boleto = models.IntegerField(primary_key=True)
    id_aluguel = models.ForeignKey(Aluguel, models.DO_NOTHING, db_column='id_aluguel', blank=True, null=True)
    id_venda = models.ForeignKey(Venda, models.DO_NOTHING, db_column='id_venda', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_proprietario = models.ForeignKey(Proprietario, models.DO_NOTHING, db_column='id_proprietario', blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    valor_boleto = models.FloatField(blank=True, null=True)
    multa_juros = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'boleto'