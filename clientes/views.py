from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required

#retornar la vista de inicio
def home(request): 
    return render(request, 'inicio.html')

#funcion para registrar nuevos usuarios
def signup(request): 

    if(request.method == 'GET'): 
        print("Enviando formulario")
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else: 
        if(request.POST['password1'] == request.POST['password2']):
            try: 
                #registrar un usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cliente')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm(),
                'error': 'Las contraseñas no coinciden'
            })

@login_required
def insertar_cliente(request):
    clientes = Cliente.objects.filter(user=request.user); 
    return render(request, 'clientes.html', {
        'clientes': clientes
    }) 

@login_required
def eliminar_cliente(request, idCliente):
    cliente = get_object_or_404(Cliente, pk=idCliente)
    if(request.method == 'POST'):
        cliente.delete()
        return redirect('cliente')

@login_required
def cliente_detalle(request, idCliente): 
   
    if(request.method == 'GET'): 
        cliente = get_object_or_404(Cliente, pk=idCliente)
        form = ClienteForm(instance=cliente)
        return render(request, 'cliente_detalle.html', {
            'cliente': cliente, 
            'form': form
        })
    else:
        cliente_update = get_object_or_404(Cliente, pk=idCliente)
        form = ClienteForm(request.POST, instance=cliente_update)
        form.save()
        return redirect('cliente')
@login_required    
def cerrarSesion(request):
    logout(request)
    return redirect('home')

def iniciarSesion(request): 
    if(request.method == 'GET'):           
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else: 
        
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])
        if user is None: 
            return render(request,'login.html', {
                'form': AuthenticationForm(),
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('cliente')

def crearCliente(request): 

    if(request.method == 'GET'):

        return render(request, 'create_cliente.html', {
            'form': ClienteForm()
        })
    else: 
        try: 
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit=False)
            nuevo_cliente.user = request.user
            nuevo_cliente.save()
            return redirect('cliente')
        except ValueError: 
            return render(request, 'create_cliente.html', {
                'form': ClienteForm(),
                'error': 'Por favor proporciona datos válidos'
            })