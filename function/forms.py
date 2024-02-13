from django import forms
from django.forms import ModelForm
from .models import VehicleCheck, PartRequest, FuelPurchase, Test
from .models import WINDSHIELD_CHOICES, WIPER_CHOICES, OIL_CHOICES, TIRE_CHOICES, HEADLIGHT_CHOICES, TAILLIGHT_CHOICES

class PartsForm (ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    parts = forms.CharField(max_length=255, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
        
    class Meta:
        model = PartRequest
        fields = ['name', 'parts']
        

class VehicleForm (ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    vehicle = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    miles = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    oil_change = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    windshield = forms.ChoiceField(choices=WINDSHIELD_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    wipers = forms.ChoiceField(choices=WIPER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    oil = forms.ChoiceField(choices=OIL_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    tires = forms.ChoiceField(choices=TIRE_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    headlights = forms.ChoiceField(choices=HEADLIGHT_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    tail_lights = forms.ChoiceField(choices=TAILLIGHT_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    additional = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = VehicleCheck
        fields = [
            'name', 'vehicle', 'miles', 
            'oil_change', 'windshield', 'wipers', 'oil', 
            'tires', 'headlights', 'tail_lights', 'additional']
        
    
class FuelForm (ModelForm):
    vehicle = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    miles = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = FuelPurchase
        fields = ['vehicle', 'miles', 'amount', 'image']
        

