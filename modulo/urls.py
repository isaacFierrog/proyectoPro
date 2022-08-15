from django.urls import path
from .views import ModuloListView, ModuloCreateView, ModuloUpdateView, ModuloDeleteView


urlpatterns = [
    path('', ModuloListView.as_view(), name='listar'), 
    path('crear/', ModuloCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', ModuloUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', ModuloDeleteView.as_view(), name='eliminar')
]