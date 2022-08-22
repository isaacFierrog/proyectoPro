from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import UsuarioModel


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Correo del usuario'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Clave del usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
        
class FormularioUsuario(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña',
                'id': 'password1',
                'required': 'required'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña de confirmacion',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nuevamente su contraseña',
                'id': 'password2',
                'required': 'required'
            }
        )
    )
    class Meta:
        model = UsuarioModel
        fields = (
            'correo',
            'nombre',
            'apellido',
            'mina',
            'zona'
        )
        widget = {
            'correo': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electronico',
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su apellido',
                    'class': 'form-control'
                }
            ),
            'mina': forms.NumberInput(
                attrs={
                    'placeholder': 'Seleccione la mina a la que sera asignado',
                    'class': 'form-control'
                }
            ),
            'zona': forms.NumberInput(
                attrs={
                    'placeholder': 'Seleccione la zona a la que sera asignado',
                    'class': 'form-control'
                }
            ),
        }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no son iguales')
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user