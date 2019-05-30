from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api_banco_dado import views

urlpatterns = [
    path('cliente/', views.ClienteList.as_view(), name="cliente_list"),
    path('cliente/<int:pk>', views.ClienteDetail.as_view(), name="cliente_detail"),
    path('corretor/', views.CorretorList.as_view(), name="corretor_list"),
    path('corretor/<int:pk>', views.CorretorDetail.as_view(), name="corretor_detail"),
    path('imovel/', views.ImovelList.as_view(), name="imovel_list"),
    path('imovel/<int:pk>', views.ImovelList.as_view(), name="imovel_detail"),
    path('proprietario/', views.ProprietarioList.as_view(),
         name="proprietario_list"),
    path('proprietario/<int:pk>', views.ProprietarioDetail.as_view(),
         name="proprietario_detail"),
]
