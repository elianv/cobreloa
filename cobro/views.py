from django.shortcuts import render

def error_404(request, exception):
    return render(request, '404.html')

def index(request):
    return render(request, '404.html')
