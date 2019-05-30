from django.urls import reverse, resolve


class TestUrls:
    """Testing url path and url name"""

    def test_cliente_list(self):
        path = reverse('cliente_list')
        assert resolve(path).view_name == 'cliente_list'

    def test_imovel_list(self):
        path = reverse('imovel_list')
        assert resolve(path).view_name == 'imovel_list'

    def test_proprietario_list(self):
        path = reverse('proprietario_list')
        assert resolve(path).view_name == 'proprietario_list'

    def test_corretor_list(self):
        path = reverse('corretor_list')
        assert resolve(path).view_name == 'corretor_list'
