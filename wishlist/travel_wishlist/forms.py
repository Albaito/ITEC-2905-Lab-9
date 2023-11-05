from django import forms
from .models import Place

class newPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = {'name', 'visited'}