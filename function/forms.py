from django import forms

class PartsForm (forms.Form):
    author = users.User
    text = forms.CharField(max_length=255, required=False)