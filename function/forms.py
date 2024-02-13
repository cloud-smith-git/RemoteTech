from django import forms
from django.forms import ModelForm
from .models import PartRequest

class PartsForm (ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    parts = forms.CharField(max_length=255, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
        
    class Meta:
        model = PartRequest
        fields = ['name', 'parts']
        
    