from django.urls import path
from .views import HomePage
from .views import Vehicle
# from .views import Part
from .views import Fuel
from .views import Test
from .views import parts_form
from . import views


app_name = 'function'

urlpatterns = [
    path('', HomePage.as_view(), name = 'index'),
    path('vehicle/', Vehicle.as_view(), name = 'vehicle'),
    path('parts/', views.parts_form, name = 'parts'),
    path('fuel/', Fuel.as_view(), name = 'fuel'),
    path('tests/', Test.as_view(), name = 'tests'),
    path('parts_form/', views.parts_form, name = 'parts_form'),
]
