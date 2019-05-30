from rest_framework import serializers
from core.models.Aluguel import Aluguel

class AluguelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluguel
        fields = ('__all__')