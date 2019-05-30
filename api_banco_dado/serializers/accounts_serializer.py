from rest_framework import serializers
from core.models.Accounts import Usuario

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')