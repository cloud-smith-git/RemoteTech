from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.shortcuts import redirect,render
from .models import VehicleCheck, PartRequest, FuelPurchase
from .forms import PartsForm, VehicleForm, FuelForm



def parts_form(request):
    if request.method == 'POST':
        form = PartsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PartsForm()
    return render(request, 'partsForm.html', {'form': form})


def vehicle_form(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = VehicleForm()
    return render(request, 'vehicleForm.html', {'form': form})


def fuel_form(request):
    if request.method == 'POST':
        form = FuelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FuelForm()
    return render(request, 'fuelForm.html', {'form': form})




class HomePage(TemplateView):
    template_name = 'home.html'

class Test(TemplateView):
    template_name = 'tests.html'