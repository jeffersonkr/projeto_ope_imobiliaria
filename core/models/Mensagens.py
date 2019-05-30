from django.db import models
from .Cliente import Cliente
from .Proprietario import Proprietario
from .Corretor import Corretor

class Mensagens(models.Model):
    #id_mensagens = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_proprietario = models.ForeignKey(Proprietario, models.DO_NOTHING, db_column='id_proprietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    assunto = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_envio = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mensagens'
