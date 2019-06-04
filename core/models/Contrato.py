from django.db import models
from core.models.Imovel import Imovel
from core.models.Cliente import Cliente


class Contrato(models.Model):
    TIPO_SERVICOS = [
        ('VE', 'Venda'),
        ('AL', 'Alugel'),
        ('VA', 'Venda e Aluguel'),
    ]

    id_imovel = models.ForeignKey(
        Imovel, on_delete=models.DO_NOTHING, db_column='id_imovel')
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, db_column='id_cliente')
    tipo_servico = models.CharField(
        max_length=2, choices=TIPO_SERVICOS, default='VA')
    periodo_contrato = models.IntegerField(db_column='periodo_contrato')
    observacao = models.CharField(max_length=200, blank=True, null=True)
