from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from .serializers import ModuloSerializer
from .forms import ModuloForm
from .models import ModuloModel


class ModuloViewSet(ModelViewSet):
    serializer_class = ModuloSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class ModuloListView(ListView):
    model = ModuloModel
    template_name = 'modulo/listar_modulo.html'
    
    
class ModuloCreateView(CreateView):
    model = ModuloModel
    form_class = ModuloForm
    template_name = 'modulo/crear_modulo.html'
    success_url = reverse_lazy('modulo:listar')
    
    
class ModuloUpdateView(UpdateView):
    model = ModuloModel
    form_class = ModuloForm
    template_name = 'modulo/crear_modulo.html'
    success_url = reverse_lazy('modulo:listar')
    
    
class ModuloDeleteView(DeleteView):
    model = ModuloModel
    template_name = 'modulo/eliminar_modulo.html'
    success_url = reverse_lazy('modulo:listar')
    
    def post(self, request, pk=None):
        modulo = self.model.objects.get(id=pk)
        modulo.delete()
        
        return self.success_url