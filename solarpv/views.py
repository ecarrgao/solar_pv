from django.shortcuts import render

def index(request):
    return render(request, 'solarpv/index.html')

def register(request):
    return render(request, 'solarpv/register.html')
