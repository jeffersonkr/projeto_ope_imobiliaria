from django.db import models
from core.models.Pessoa import Pessoa

class Cliente(Pessoa):
    pessoa_juridica = models.BooleanField(default=False)
    inquilino = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'cliente'
