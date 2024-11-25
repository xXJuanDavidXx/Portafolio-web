from django import forms


class Info_contacto(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre',
            'class': 'form-control',
            'style': 'color: white; background-color: #212529;'
        }),
        label=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            'style': 'color: white; background-color: #212529;'
        }),
        label=''
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Mensaje',
            'class': 'form-control',
            'style': 'color: white; background-color: #212529;'
        }),
        label=''
    )
