from dataclasses import field
from django import forms
from .models import ModuloModel


class ModuloForm(forms.ModelForm):
    class Meta:
        model = ModuloModel
        fields = '__all__'
        read_only_fields = ('id',)
        widgets = {
            'mac': forms.TextInput(attrs={
                'placeholder': 'Ingrese la mac del modulo',
                'class': 'form-control'
            }),
            'mina': forms.Select(attrs={
                'placeholder': 'Ingrese la mina a la cual esta destinada el modulo',
                'class': 'form-control'
            }),
            'area': forms.Select(attrs={
                'placeholder': 'Ingrese el area a la cual esta destinada el modulo',
                'class': 'form-control'
            })
        }