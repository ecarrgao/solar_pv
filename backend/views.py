from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from backend.models import TestStandard

class TestStandardList(ListView):
    model = TestStandard

class TestStandardView(DetailView):
    model = TestStandard

class TestStandardCreate(CreateView):
    model = TestStandard
    fields = ['standard_name', 'description', 'published_date']
    success_url = reverse_lazy('teststandard_list')

class TestStandardUpdate(UpdateView):
    model = TestStandard
    fields = ['standard_name', 'description', 'published_date']
    success_url = reverse_lazy('teststandard_list')

class TestStandardDelete(DeleteView):
    model = TestStandard
    success_url = reverse_lazy('teststandard_list')
