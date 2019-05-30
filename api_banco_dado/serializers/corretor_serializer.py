from rest_framework import serializers
from core.models.Corretor import Corretor

class CorretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corretor
        fields = ('__all__')