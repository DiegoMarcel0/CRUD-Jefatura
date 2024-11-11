from django import forms
from .models import Empleado, oficiales, registro_casos, reportes_caso, reportes_de_servicio
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.core.exceptions import ValidationError


##CREACION DE COSOS
"""
class CustomUserLoginForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Empleado
        fields = UserChangeForm.Meta.fields
        #fields = ['username', 'first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone', 'password']
"""
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Empleado
        fields = ['first_name', 'last_name','last_name2', 'email', 'puesto', 'register_date', 'num_phone']
        #fields = UserCreationForm.Meta.fields
"""
class CustomUserCreationForm2(UserCreationForm):

    class Meta(UserCreationForm):
        model = Empleado
        fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone', 'username']
"""
class OficialesForm(forms.ModelForm):
    class Meta:
        model = oficiales
        fields = ['id_emp', 'rank']
        #fields = ['first_name', 'last_name', 'email', 'puesto', 'register_date', 'num_phone']
class CasosForm(forms.ModelForm):
    class Meta:
        model = registro_casos
        fields = '__all__'

class ReporteCasoForm(forms.ModelForm):
    class Meta:
        model = reportes_caso
        fields = ['titulo', 'contenido','fecha_reporte', 'tipo']

class ReporteServicioForm(forms.ModelForm):
    class Meta:
        model = reportes_de_servicio
        fields = '__all__'
        
#EDITAR
class EmpleadoUpdateForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['first_name', 'last_name', 'email', 'puesto', 'num_phone', 'username']
class OficialesUpdateForm(forms.ModelForm):
    class Meta:
        model = oficiales
        fields = ['rank']
class CasoUpdateForm(CasosForm):
    pass
class ReporteServicioUpdateForm(ReporteServicioForm):
    pass
class ReporteCasoUpdateForm(ReporteCasoForm):
    pass

#DETALLES
class DetailBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

class EmpleadoDetailForm(DetailBaseForm):
    class Meta:
        model = Empleado
        fields = ['first_name', 'last_name','last_name2', 'email', 'puesto', 'register_date', 'num_phone']

class OficialDetailForm(DetailBaseForm):
    class Meta:
        model = oficiales
        fields = '__all__'
class CasosDetailForm(DetailBaseForm):
    class Meta:
        model = registro_casos
        fields = '__all__'
class ReporteServicioDetailForm(DetailBaseForm):
    class Meta:
        model = reportes_de_servicio
        fields = '__all__'
class ReporteCasoDetailForm(DetailBaseForm):
    class Meta:
        model = reportes_caso
        fields = '__all__'