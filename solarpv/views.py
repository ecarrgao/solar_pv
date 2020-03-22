from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from solarpv.forms import RegistrationForm


def index(request):
    return render(request, 'solarpv/index.html')

def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'solarpv/register.html', context)

def dashboard(request):
    return render(request, 'solarpv/dashboard.html')

def signin(request):
    return render(request, 'solarpv/signin.html')
