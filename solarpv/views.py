from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from solarpv.forms import RegistrationForm, LoginForm


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

def logout_view(request):
    logout(request)
    return redirect('index')

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_staff:
            return redirect('dashboard')
        else:
            return redirect('index')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user.is_staff:
                login(request, user)
                return redirect('dashboard')
            elif user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'solarpv/login.html', context)
