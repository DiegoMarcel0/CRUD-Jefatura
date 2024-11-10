from django import forms
from .models import Empleado, oficiales, registro_casos, reportes_caso, reportes_de_servicio
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.core.exceptions import ValidationError

class CustomUserLoginForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Empleado
        fields = UserChangeForm.Meta.fields
        #fields = ['username', 'first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone', 'password']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Empleado
        fields = ['first_name', 'last_name','last_name2', 'email', 'puesto', 'register_date', 'num_phone']
        #fields = UserCreationForm.Meta.fields
class CustomUserCreationForm2(UserCreationForm):

    class Meta(UserCreationForm):
        model = Empleado
        fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone', 'username']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Empleado
        fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone', 'username']

class EmpleadoDetail(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone', 'username']

class OficialesForm(forms.ModelForm):
    class Meta:
        model = oficiales
        fields = ['id_emp', 'rank']
        #fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone']
class OficialesUpdateForm(forms.ModelForm):
    class Meta:
        model = oficiales
        fields = ['rank']

class CasosForm(forms.ModelForm):
    class Meta:
        model = registro_casos
        fields = '__all__'
        #fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone']

class ReporteCasoForm(forms.ModelForm):
    class Meta:
        model = reportes_caso
        fields = '__all__'
        #fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone']

class ReporteServicioForm(forms.ModelForm):
    class Meta:
        model = reportes_de_servicio
        fields = '__all__'
        #fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone']
"""
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        #fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone']
"""