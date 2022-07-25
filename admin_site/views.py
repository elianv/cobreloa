from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from admin_site.forms import LoginForm

# Create your views here.
def login_view(request):

    form = LoginForm

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
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