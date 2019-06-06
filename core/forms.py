from django.forms import ModelForm
from core.models.contato2 import Contato


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "sobrenome", "email", "telefone", "mensagem"]
