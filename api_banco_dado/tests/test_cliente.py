from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse, resolve
from core.models.Cliente import Cliente
from api_banco_dado.serializers.cliente_serializer import ClienteSerializer


class GetAllCustomers(TestCase):
    """ Test module for GET all employees API """

    def set_up(self):
        Cliente.objects.create(
            name='Casper',
            cpf='268.464.123-31',
            rg='23692358-6',
            endereco='Rua Sergio Tomas, 422',
            bairro='Bom Retiro',
            cidade='São Paulo',
            cep='01122-000',
            uf='SP',
            telefone='11941042323',
            email='casper@gmail.com',
            pessoa_juridica=False,
            inquilino=True
        )

    def test_get_all_employees(self):
        client = Client()
        # get API response
        response = client.get(reverse('cliente_list'))
        # get data from db
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
