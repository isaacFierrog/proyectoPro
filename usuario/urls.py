from django.urls import path
from .views import RegistrarUsuario, ListarUsuario


urlpatterns = [
    path('crear/', RegistrarUsuario.as_view(), name='crear'),
    path('listar/', ListarUsuario.as_view(), name='listar')
]