
from django.db import models


class Contato(models.Model):

    nome = models.CharField(max_length=30, blank=True)
    sobrenome = models.CharField(max_length=60, blank=True)
    email = models.EmailField(unique=False,blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    mensagem = models.TextField(blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome



class Anuncie(models.Model):
    nome = models.CharField(max_length=30, blank=True)
    telefone = models.CharField(max_length=30, blank=True)

    TIPO_SERVICOS = [
        ('VE', 'Venda'),
        ('AL', 'Alugel'),
        ('VA', 'Venda e Aluguel'),
    ]
    tipo_servico = models.CharField(blank=True,max_length=2, choices=TIPO_SERVICOS, default='VA')


    FINALIDADE = [
        ('RE', 'Residencial'),
        ('CO', 'Comercial'),
    ]

    finalidade = models.CharField(blank=True,max_length=2, choices=FINALIDADE, default='RE')
    
    endereco = models.CharField(blank=True,max_length=100)
    bairro = models.CharField(blank=True,max_length=50)
    cidade = models.CharField(blank=True,max_length=50)
    cep = models.CharField(blank=True,max_length=9)
    metro = models.CharField(blank=True,max_length=50)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_venda = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qtd_comodo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome + ' ' + self.bairro




