from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Bienvenidos a GESTION DE TIENDA')
def show_login(request):
    return render(request,'login.html')