from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'

class Vehicle(TemplateView):
    template_name = 'vehicle.html'

class Fuel(TemplateView):
    template_name = 'fuel.html'

class Part(TemplateView):
    template_name = 'parts.html'

class Test(TemplateView):
    template_name = 'tests.html'