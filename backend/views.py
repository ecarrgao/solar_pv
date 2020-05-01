from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from solarpv.models import Client
from backend.models import Location, Product, TestStandard, Certificate

def dashboard(request):
    return render(request, 'backend/dashboard.html')

#Client views
class ClientList(ListView):
    model = Client

class ClientView(DetailView):
    model = Client

class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client_list')

class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client_list')

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')

#location Views
class LocationList(ListView):
    model = Location

class LocationView(DetailView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('location_list')

class LocationUpdate(UpdateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('location_list')

class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('location_list')

#product Views
class ProductList(ListView):
    model = Product

class ProductView(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


#Test Standard Views
class TestStandardList(ListView):
    model = TestStandard

class TestStandardView(DetailView):
    model = TestStandard

class TestStandardCreate(CreateView):
    model = TestStandard
    fields = '__all__'
    success_url = reverse_lazy('teststandard_list')

class TestStandardUpdate(UpdateView):
    model = TestStandard
    fields = '__all__'
    success_url = reverse_lazy('teststandard_list')

class TestStandardDelete(DeleteView):
    model = TestStandard
    success_url = reverse_lazy('teststandard_list')

#certificate Views
class CertificateList(ListView):
    model = Certificate

class CertificateView(DetailView):
    model = Certificate

class CertificateCreate(CreateView):
    model = Certificate
    fields = '__all__'
    success_url = reverse_lazy('certificate_list')

class CertificateUpdate(UpdateView):
    model = Certificate
    fields = '__all__'
    success_url = reverse_lazy('certificate_list')

class CertificateDelete(DeleteView):
    model = Certificate
    success_url = reverse_lazy('certificate_list')
