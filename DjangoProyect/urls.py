"""
URL configuration for DjangoProyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clientes import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('cliente/', views.insertar_cliente, name='cliente'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
    path('cliente/detalle/<int:idCliente>/', views.cliente_detalle, name='cliente_detalle'),
    path('cliente/<int:idCliente>/delete', views.eliminar_cliente, name='cliente_eliminar'),
]