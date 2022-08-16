from django.urls import path
from .views import RegistrarUsuario, ListarUsuario, UsuarioUpdateView


urlpatterns = [
    path('crear/', RegistrarUsuario.as_view(), name='crear'),
    path('listar/', ListarUsuario.as_view(), name='listar'),
    path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar')
]