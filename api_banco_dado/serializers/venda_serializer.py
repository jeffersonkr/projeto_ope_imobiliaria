from rest_framework import serializers
from core.models.Venda import Venda

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ('__all__')