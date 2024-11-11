from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import EmpleadoUpdateForm, CustomUserCreationForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = EmpleadoUpdateForm
    model = Empleado

admin.site.register(registro_casos)
admin.site.register(Empleado)
admin.site.register(oficiales)
admin.site.register(reportes_caso)