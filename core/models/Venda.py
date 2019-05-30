from django.db import models
from .Cliente import Cliente
from .Proprietario import Proprietario
from .Imovel import Imovel
from .Corretor import Corretor

class Venda(models.Model):
    #id_venda = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey(Proprietario, models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_imovel = models.ForeignKey(Imovel, models.DO_NOTHING, db_column='Id_imovel', blank=True, null=True)  # Field name made lowercase.
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True)
    valor_imovel = models.FloatField(blank=True, null=True)
    valor_venda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'venda'