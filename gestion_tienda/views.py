from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        usuarioInfo = authenticate(request, username=nombreUsuario, password=passwordUsuario)
        if usuarioInfo is not None:
            login(request,usuarioInfo)
            return HttpResponseRedirect(reverse('gestion_tienda:consolaAdministrador'))
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='http://127.0.0.1:8000')
def consolaAdministrador(request):
    return render(request,'consolaAdministrador.html')
