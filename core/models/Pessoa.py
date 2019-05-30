from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=14, blank=True, unique=True)
    rg = models.CharField(max_length=30, blank=True, unique=True)
    cnpj = models.CharField(max_length=18, blank=True, unique=True)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    uf = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)
    email = models.EmailField()

    class Meta:
        abstract = True