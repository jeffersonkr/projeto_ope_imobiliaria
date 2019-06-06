
from django.db import models


class Contato(models.Model):

    nome = models.CharField(max_length=30, blank=True)
    sobrenome = models.CharField(max_length=60, blank=True)
    email = models.EmailField(unique=False)
    telefone = models.CharField(max_length=30, blank=True)
    mensagem = models.TextField(blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
