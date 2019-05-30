from django.db import models
from .Cliente import Cliente
from .Imovel import Imovel
from .Proprietario import Proprietario
from .Corretor import Corretor

class Endereco(models.Model):
    #id_endereco = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente', blank=True, null=True)
    id_imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, db_column='id_imovel', blank=True, null=True)
    id_proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, db_column='id_proprietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE, db_column='id_corretor', blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'endereco'