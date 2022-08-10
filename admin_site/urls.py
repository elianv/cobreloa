from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login' ),
    path('login', views.login_view, name='login_view' ),
    path('main', views.index, name='main'),
    path('logout', views.logout_view, name='logout'),
    path('crear_socio', views.crear_socio, name='crear_socio'),
    path('listar_socios', views.listar_socios, name='listar_socios'),
    path('listar_socios_ajax', views.listar_socios_ajax, name='listar_socios_ajax'),
] 
