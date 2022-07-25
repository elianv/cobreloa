from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login' ),
    path('login', views.login_view, name='login_view' ),
    path('main', views.index, name='main'),
    path('logout', views.logout_view, name='logout')
] 
