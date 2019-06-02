from django.db import models
from core.models.Pessoa import Pessoa


class Cliente(Pessoa):
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    pessoa_juridica = models.BooleanField(default=False)
    inquilino = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'cliente'
