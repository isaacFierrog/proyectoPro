from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from usuario.views import Login, logout_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'index'))),
    path('api/', include('modulo.routers')),
    path('api/', include('sensor.routers')),
    path("modulo/", include(('modulo.urls', 'modulo'))),
    path('usuario/', include(('usuario.urls', 'usuario'))),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logout_usuario), name='logout')
]
