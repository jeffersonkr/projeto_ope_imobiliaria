from django.db import models
from .Cliente import Cliente
from .Proprietario import Proprietario
from .Imovel import Imovel
from .Corretor import Corretor

class Aluguel(models.Model):
    #id_aluguel = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_proprietario = models.ForeignKey(Proprietario, models.DO_NOTHING, db_column='id_proprietario', blank=True, null=True)
    id_imovel = models.ForeignKey(Imovel, models.DO_NOTHING, db_column='id_imovel', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    data_aluguel = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    contrato = models.CharField(max_length=100, blank=True, null=True)
    valor_aluguel = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aluguel'
