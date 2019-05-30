from django.db import models
from core.models.Pessoa import Pessoa

class Proprietario(Pessoa):
    pessoa_juridica = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        db_table = 'proprietario'
