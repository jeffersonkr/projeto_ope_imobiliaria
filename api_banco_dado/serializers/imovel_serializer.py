from rest_framework import serializers
from core.models.Imovel import Imovel

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ('__all__')