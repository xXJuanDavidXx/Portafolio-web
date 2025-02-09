from django import forms
from .models import Category

class Buscar(forms.Form):
    query = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm text-white',  # Bordes redondeados y sombra
            'placeholder': 'Buscar...',
            'aria-label': 'Search'
        })                        
    )
    
    category = forms.ModelChoiceField(
        label="", 
        queryset=Category.objects.all(),
        required=False, 
        empty_label="--categoria--",
        widget=forms.Select(attrs={
            'class': 'form-select border-0 shadow-sm bg-dark text-white',  # Bordes redondeados y sombra
            'aria-label': 'Dropdown',
            'style' : 'height: 50px'
        })
    )
