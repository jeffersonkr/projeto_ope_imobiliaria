from django.db import models
from .Cliente import Cliente
from .Proprietario import Proprietario
from .Corretor import Corretor

class Contato(models.Model):
    #id_contato = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente', blank=True, null=True)
    id_proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, db_column='id_proprietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE, db_column='id_corretor', blank=True, null=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contato'