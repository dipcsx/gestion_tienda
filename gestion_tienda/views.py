from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import bl_user, bl_producto
# Create your views here.

def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('username')
        passwordUsuario = request.POST.get('password')
        usuarioInfo = authenticate(request, username=nombreUsuario, password=passwordUsuario)
        if usuarioInfo is not None:
            login(request,usuarioInfo)
            if usuarioInfo.bl_user.rolUsuario == 'ADMINISTRADOR':
                return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuario'))
            else:
                return HttpResponseRedirect(reverse('gestion_tienda:verProducto', kwargs={'ind':usuarioInfo.id}))
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='http://127.0.0.1:8000')
def gestionUsuario(request):
    if request.user.bl_user.rolUsuario == 'ADMINISTRADOR':
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            nombres=request.POST.get('nombres')
            apellidos=request.POST.get('apellidos')
            email=request.POST.get('email')
            roluser=request.POST.get('roluser')
            nrocelular=request.POST.get('nrocelular')
            usuarionuevo=User.objects.create(
                username=username,
                email=email,
            )
            usuarionuevo.set_password(password)
            usuarionuevo.first_name = nombres
            usuarionuevo.last_name = apellidos
            usuarionuevo.is_staff=True
            usuarionuevo.save()
            bl_user.objects.create(
                usuario=usuarionuevo,
                rolUsuario=roluser,
                nroCelular=nrocelular,
            )
            return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuario'))
        return render(request,'gestionUsuario.html',{
            'usuariosTotales':User.objects.all().order_by('id')
        })
    else:
        return HttpResponseRedirect(reverse('gestion_tienda:verProducto',kwargs={'ind':request.user.id}))

@login_required(login_url='http://127.0.0.1:8000')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tienda:index'))

def eliminarUsuario(request,ind):
    usuarioEliminar = User.objects.get(id=ind)
    bl_user.objects.get(usuario=usuarioEliminar).delete()
    usuarioEliminar.delete()
    return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuario'))

@login_required(login_url='http://127.0.0.1:8000')
def verProducto(request,ind):
    usuarioInformacion=User.objects.get(id=ind)
    productosUser=bl_producto.objects.filter(usuarioProducto=usuarioInformacion).order_by('id')
    return render(request,'gestionProducto.html',{
        'usuarioInfo': usuarioInformacion,
        'productosUser': productosUser
    })

def nuevoProducto(request,ind):
    if request.method == 'POST':
        usuarioProducto = User.objects.get(id=ind)
        nombProducto = request.POST.get('nombproducto')
        codProducto = request.POST.get('codproducto')
        pCompra = request.POST.get('pcompra')
        pVenta = request.POST.get('pventa')
        bl_producto.objects.create(
            usuarioProducto = usuarioProducto,
            nombProducto = nombProducto,
            codProducto = codProducto,
            precioCompra = pCompra,
            precioVenta = pVenta,
        )
        return HttpResponseRedirect(reverse('gestion_tienda:verProducto', kwargs={'ind':ind}))

def eliminarProducto(request,idProducto,idUsuario):
    bl_producto.objects.get(id=idProducto).delete()
    return HttpResponseRedirect(reverse('gestion_tienda:verProducto',kwargs={'ind':idUsuario}))