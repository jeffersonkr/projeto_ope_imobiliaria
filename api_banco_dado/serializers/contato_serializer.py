from rest_framework import serializers
from core.models.Contato import Contato

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('__all__')