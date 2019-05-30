from rest_framework import serializers
from core.models.Proprietario import Proprietario

class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = ('__all__')