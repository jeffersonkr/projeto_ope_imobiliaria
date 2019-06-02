from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=30, unique=True)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    uf = models.CharField(max_length=10)
    telefone = models.CharField(max_length=16)
    email = models.EmailField()

    class Meta:
        abstract = True

    def __str__(self):
        """Representation of object, person name."""

        return self.nome

    def _capitalize_attributes(self, attribute):
        """Capitalize attributes."""

        return " ".join([i.capitalize() for i in attribute.split()])

    def save(self, *args, **kwargs):
        """Capitalize attributes and then save."""

        self.nome = self._capitalize_attributes(self.nome)
        self.endereco = self._capitalize_attributes(self.endereco)
        self.bairro = self._capitalize_attributes(self.bairro)
        self.cidade = self._capitalize_attributes(self.cidade)
        self.uf = self.uf.upper()
        super(Pessoa, self).save(*args, **kwargs)
