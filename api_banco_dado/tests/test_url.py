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

    def test_cliente_detail(self):
        path = reverse('cliente_detail', args=[1])
        assert resolve(path).view_name == 'cliente_detail'

    def test_imovel_detail(self):
        path = reverse('imovel_detail', args=[1])
        assert resolve(path).view_name == 'imovel_detail'

    def test_proprietario_detail(self):
        path = reverse('proprietario_detail', args=[1])
        assert resolve(path).view_name == 'proprietario_detail'

    def test_corretor_detail(self):
        path = reverse('corretor_detail', args=[1])
        assert resolve(path).view_name == 'corretor_detail'
