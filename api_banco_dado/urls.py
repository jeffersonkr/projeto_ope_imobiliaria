from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views
from api_banco_dado import views

urlpatterns = [
    path('cliente/', views.ClienteList.as_view(), name="cliente_list"),
    path('cliente/<int:pk>', views.ClienteDetail.as_view(), name="cliente_detail"),
    path('corretor/', views.CorretorList.as_view(), name="corretor_list"),
    path('corretor/<int:pk>', views.CorretorDetail.as_view(), name="corretor_detail"),
    path('imovel/', views.ImovelList.as_view(), name="imovel_list"),
    path('imovel/<int:pk>', views.ImovelDetail.as_view(), name="imovel_detail"),
    path('proprietario/', views.ProprietarioList.as_view(),
         name="proprietario_list"),
    path('proprietario/<int:pk>', views.ProprietarioDetail.as_view(),
         name="proprietario_detail"),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
