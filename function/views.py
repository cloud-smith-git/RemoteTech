from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user
from django import forms

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
        form = FuelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FuelForm()
    return render(request, 'fuelForm.html', {'form': form})

class HomePage(TemplateView):
    template_name = 'home.html'

# class Vehicle(TemplateView):
    # template_name = 'vehicle.html'

# class Fuel(TemplateView):
    # template_name = 'fuel.html'

# class Part(TemplateView):
    # template_name = 'partsForm.html'

class Test(TemplateView):
    template_name = 'tests.html'