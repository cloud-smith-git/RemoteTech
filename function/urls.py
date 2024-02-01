from django.urls import path
from .views import HomePage
from .views import Vehicle
from .views import Part
from .views import Fuel
from .views import Test
from . import views


app_name = 'function'

urlpatterns = [
    path('', HomePage.as_view(), name = 'index'),
    path('vehicle/', Vehicle.as_view(), name = 'vehicle'),
    path('parts/', views.Part.as_view(), name = 'parts'),  #The fact that the path includes parts, but the model is Part doesn't effect it
    path('fuel/', Fuel.as_view(), name = 'fuel'),
    path('tests/', Test.as_view(), name = 'tests'),
    
    
]
