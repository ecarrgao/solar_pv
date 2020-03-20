from django.shortcuts import render

def index(request):
    return render(request, 'solarpv/index.html')

def register(request):
    return render(request, 'solarpv/register.html')

def dashboard(request):
    return render(request, 'solarpv/dashboard.html')

def signin(request):
    return render(request, 'solarpv/signin.html')
