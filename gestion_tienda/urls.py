from django.urls import path, include
from . import views

app_name = 'gestion_tienda'

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.show_login,name='pg_login')
]