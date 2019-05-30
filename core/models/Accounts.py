from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.nome + " " + self.email