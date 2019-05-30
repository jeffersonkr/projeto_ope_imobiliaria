from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_banco_dado.serializers.cliente_serializer import ClienteSerializer
from api_banco_dado.serializers.corretor_serializer import CorretorSerializer
from api_banco_dado.serializers.imovel_serializer import ImovelSerializer
from api_banco_dado.serializers.proprietario_serializer import ProprietarioSerializer
from core.models.Cliente import Cliente
from core.models.Corretor import Corretor
from core.models.Imovel import Imovel
from core.models.Proprietario import Proprietario


class ClienteList(APIView):
    '''List all customer, or create a new customer.'''

    def get(self, request, format=None):
        """List all employees"""

        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new employee"""

        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):
    """Retrieve, update or delete an customer instance."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProprietarioList(APIView):
    '''List all owners, or create a new owner.'''

    def get(self, request, format=None):
        """List all owners"""

        proprietario = Proprietario.objects.all()
        serializer = ProprietarioSerializer(proprietario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new employee"""

        serializer = ProprietarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProprietarioDetail(APIView):
    """Retrieve, update or delete an owner instance."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Proprietario.objects.get(pk=pk)
        except Proprietario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        proprietario = self.get_object(pk)
        serializer = ProprietarioSerializer(proprietario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        proprietario = self.get_object(pk)
        serializer = ProprietarioSerializer(proprietario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proprietario = self.get_object(pk)
        proprietario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImovelList(APIView):
    '''List all realty, or create a new realty.'''

    def get(self, request, format=None):
        """List all realty"""

        imoveis = Imovel.objects.all()
        serializer = ImovelSerializer(imoveis, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new realty"""

        serializer = ImovelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImovelDetail(APIView):
    """Retrieve, update or delete an realty instance."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Imovel.objects.get(pk=pk)
        except Imovel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        imovel = self.get_object(pk)
        serializer = ImovelSerializer(imovel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        imovel = self.get_object(pk)
        serializer = ImovelSerializer(imovel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        imovel = self.get_object(pk)
        imovel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CorretorList(APIView):
    '''List all realty, or create a new realty.'''

    def get(self, request, format=None):
        """List all realty"""

        corretores = Corretor.objects.all()
        serializer = CorretorSerializer(corretores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new realty"""

        serializer = CorretorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CorretorDetail(APIView):
    """Retrieve, update or delete an realty instance."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Corretor.objects.get(pk=pk)
        except Corretor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        corretor = self.get_object(pk)
        serializer = ImovelSerializer(corretor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        corretor = self.get_object(pk)
        serializer = CorretorSerializer(corretor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        corretor = self.get_object(pk)
        corretor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
