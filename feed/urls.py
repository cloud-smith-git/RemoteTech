from django.urls import path
from .views import HomePage
from .views import Vehicle
from .views import Parts
from .views import Fuel
from .views import Testing



app_name = 'feed'

urlpatterns = [
    path('', HomePage.as_view(), name = 'index'),
    path('vehicle/', Vehicle.as_view(), name = 'vehicle'),
    path('parts/', Parts.as_view(), name = 'parts'),
    path('fuel/', Fuel.as_view(), name = 'fuel'),
    path('testing/', Testing.as_view(), name = 'testing'),

]
