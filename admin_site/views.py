from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from admin_site.forms import LoginForm
from socios.forms import SocioForm
from socios.models import Socio, Cuota

from itertools import cycle
from datetime import date
import json

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    
    if request.user.is_authenticated:
        return redirect('main')
    
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        
        user = form.login(request)
        
        if user:
            login(request, user)
            return redirect('main')

    data = { 'form': form }

    return render(request, 'login.html', data)

@login_required
def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def crear_socio(request):
    
    if request.method == 'POST':

        form = SocioForm(request.POST or None, request.FILES)
        if form.data['rut'].find('-') < 0:
            form.add_error('rut', 'Error en el formato. Falta el guion (-)')
            form.fields['dv'] = form.fields['rut'].split("-")[1]

        if form.is_valid():
            a = form.save()
            crear_cuotas_socio(a)
            messages.success(request, 'Contact request submitted successfully.')
    else:        
        form = SocioForm(request.POST or None)
        
    data = {'form': form, 'title': 'Registro', 'small_title': 'nuevo socio'}
    return render(request, 'registro_socios.html', data)

@login_required
def listar_socios(request):
    data = {'title': 'Ver', 'small_title': 'socios'}
    return render(request, 'listado_socios.html', data)

def crear_cuotas_socio(socio):
    meses = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    valor_cuota = 3000
    current_year = date.today().year
    
    try:
        for m in meses:
            c = Cuota(socio=socio, mes=m, anio=current_year, monto=valor_cuota, estado='n' )
            c.save()
        return True
    except Exception as e:
        return e    
    

@login_required
def listar_socios_ajax(request):

    if request.method == 'GET':
        socios = Socio.objects.all()
        response = {"data": list(socios.values_list('rut', 'numero_socio', 'nombres', 'estado', 'deuda'))}
        return JsonResponse(response, status=200, safe=False)
    else:
        return HttpResponseBadRequest('Invalid request')    
    

def _validarRut(rut):
	rut = rut.upper();
	rut = rut.replace("-","")
	rut = rut.replace(".","")
	aux = rut[:-1]
	dv = rut[-1:]
 
	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11
 
	if str(res) == dv:
		return True
	elif dv=="K" and res==10:
		return True
	else:
		return False