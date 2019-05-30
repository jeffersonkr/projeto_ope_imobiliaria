from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', sair, name='logout'),
    path('register/', registrar, name='register'),
    path('sistema/', home_sistema, name='home-sistema'),
    path('cadastro/',cadastro, name='cadastro'),
    path('cadastro/usuarios/', cadastro_clientes, name='cadastro-usuarios'),
    path('cadastro/clientes/', cadastro_clientes, name='cadastro-clientes'),
    path('cadastro/imoveis/', cadastro_imoveis, name='cadastro-imoveis'),
    path('cadastro/corretores/', cadastro_corretores, name='cadastro-corretores'),
    path('cadastro/proprietarios/', cadastro_proprietario, name='cadastro-proprietarios'),
    path('cadastro/delete_cliente/<int:pk>/', delete_cliente, name='delete_cliente'),
    path('cadastro/delete_corretor/<int:pk>/', delete_corretor, name='delete_corretor'),
    path('cadastro/delete_imovel/<int:pk>/', delete_imovel, name='delete_imovel'),
    path('cadastro/delete_proprietario/<int:pk>/', delete_proprietario, name='delete_cliente'),
    path('cadastro/atualizar_view_cliente/<int:pk>/', atualizar_view_cliente, name='atualizar_view_cliente'),
    path('cadastro/atualizar_view_imovel/<int:pk>/', atualizar_view_imovel, name='atualizar_view_imovel'),
    path('cadastro/atualizar_view_proprietario/<int:pk>/', atualizar_view_proprietario, name='atualizar_view_proprietario'),
]