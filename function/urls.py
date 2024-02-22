from django.urls import path
from .views import HomePage
from .views import vehicle_form, parts_form, fuel_form
from . import views


app_name = 'function'

urlpatterns = [
    path('', HomePage.as_view(), name = 'index'),
    path('vehicle/', views.vehicle_form, name = 'vehicle'),
    path('parts/', views.parts_form, name = 'parts'),
    path('fuel/', views.fuel_form, name = 'fuel'), 
    path('tests/', views.Test.as_view(), name = 'tests'),
    path('parts_form/', views.parts_form, name = 'parts_form'),
    path('vehicle_form/', views.vehicle_form, name = 'vehicle_form'),
    path('fuel_form/', views.fuel_form, name = 'fuel_form'),
    
]
