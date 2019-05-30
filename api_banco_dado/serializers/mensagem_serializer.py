from rest_framework import serializers
from core.models.Mensagens import Mensagens

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagens
        fields = ('__all__')
