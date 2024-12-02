from django import forms
from .models import Empleado, oficiales, registro_casos, reportes_caso, reportes_de_servicio
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.core.exceptions import ValidationError


##CREACION DE COSOS
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Empleado
        fields = ['first_name', 'last_name','last_name2', 'email', 'puesto', 'register_date', 'num_phone', 'salario']
        widgets = {
            'register_date': forms.DateInput(attrs={'type': 'date'}), 
        }

class OficialesForm(forms.ModelForm):
    class Meta:
        model = oficiales
        fields = ['id_emp', 'rank']
class CasosForm(forms.ModelForm):
    class Meta:
        model = registro_casos
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),  
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),  
        }

class ReporteCasoForm(forms.ModelForm):
    class Meta:
        model = reportes_caso
        fields = ['titulo', 'contenido','fecha_reporte', 'tipo']
        widgets = {
            'fecha_reporte': forms.DateInput(attrs={'type': 'date'}),  
        }

class ReporteServicioForm(forms.ModelForm):
    class Meta:
        model = reportes_de_servicio
        fields = ['titulo', 'contenido','tipo', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}), 
        }
        
#EDITAR
class EmpleadoUpdateForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['first_name', 'last_name', 'email', 'puesto', 'num_phone', 'salario', 'username']
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
        fields = ['first_name', 'last_name','last_name2', 'email', 'puesto', 'register_date', 'num_phone', 'salario']

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