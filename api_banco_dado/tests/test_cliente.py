from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse, resolve
from core.models.Cliente import Cliente
from api_banco_dado.serializers.cliente_serializer import ClienteSerializer


_client = Client()


class TestCustomers(TestCase):
    """ Test module for GET all employees API """

    def setUp(self):
        """set up cliente for test"""

        Cliente.objects.create(
            nome='Casper',
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

    def test_get_all_customers(self):
        """Test to get all customers."""

        response = _client.get(reverse('cliente_list'))
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_customer(self):
        """Test to get cliente with pk equal 1."""

        response = _client.get(reverse('cliente_detail', args=[1]))
        cliente = Cliente.objects.get(id=1)
        serializer = ClienteSerializer(cliente, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
