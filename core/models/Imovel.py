from django.db import models
from core.models.Cliente import Cliente
from core.models.Proprietario import Proprietario
from core.models.Corretor import Corretor

class Imovel(models.Model):
    TIPO_SERVICOS = [
        ('VE', 'Venda'),
        ('AL', 'Alugel'),
        ('VA', 'Venda e Aluguel'),
        ]

    STATUS_IMOVEL = [
        ('AL', 'Alugado'),
        ('DI', 'Disponivel'),
        ('IN', 'Indisponivel'),
    ]

    id_proprietario = models.ForeignKey(Proprietario, models.DO_NOTHING, db_column='id_proprietario')
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    matricula = models.IntegerField()
    residencial = models.BooleanField(default=False)
    qtd_comodo = models.IntegerField()
    n_sabesp = models.CharField(max_length=30)
    n_eletropaulo = models.CharField(max_length=30)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_venda = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    iptu = models.DecimalField(max_digits=10, decimal_places=2)
    metragem = models.IntegerField()
    tipo_servico = models.CharField(max_length=2, choices=TIPO_SERVICOS, default='VA')
    status_imovel = models.CharField(max_length=2, choices=STATUS_IMOVEL, default='DI')
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.TextField()
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    uf = models.CharField(max_length=100)
    imagem_1 = models.ImageField(upload_to=f'imovel/{matricula}/', 
                            default=f"{matricula}_foto_1", blank=True, null=True)
    imagem_2 = models.ImageField(upload_to=f'imovel/{matricula}/', 
                            default=f"{matricula}_foto_2", blank=True, null=True)
    imagem_3 = models.ImageField(upload_to=f'imovel/{matricula}/', 
                            default=f"{matricula}_foto_3", blank=True, null=True)
    imagem_4 = models.ImageField(upload_to=f'imovel/{matricula}/', 
                            default=f"{matricula}_foto_4", blank=True, null=True)
    imagem_5 = models.ImageField(upload_to=f'imovel/{matricula}/', 
                            default=f"{matricula}_foto_5", blank=True, null=True)

    

    class Meta:
        managed = True
        db_table = 'imovel'
