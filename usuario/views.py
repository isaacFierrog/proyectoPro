from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin, FormularioUsuario
from .models import UsuarioModel


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index:home')
    
    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url())
        else:
            return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
    
    
def logout_usuario(request):
    logout(request)
    return redirect('login')


class RegistrarUsuario(CreateView):
    model = UsuarioModel
    form_class = FormularioUsuario
    success_url = reverse_lazy('usuario:listar')
    template_name = 'usuario/crear_usuario.html'
    
    
class ListarUsuario(ListView):
    model = UsuarioModel
    template_name = 'usuario/listar_usuario.html'
    ordering = ('-id',)
    
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
    
class UsuarioUpdateView(UpdateView):
    model = UsuarioModel
    form_class = FormularioUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuario:listar')
    
    
class EliminarUsuario(DeleteView):
    model = UsuarioModel
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy('usuario:listar')
    
    def post(self, request, pk=None):
        usuario = self.model.objects.get(id=pk)
        usuario.is_active = False
        usuario.save()
        
        return redirect('usuario:listar')