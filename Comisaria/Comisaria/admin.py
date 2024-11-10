from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Empleado, registro_casos, oficiales

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Empleado

admin.site.register(registro_casos)
admin.site.register(Empleado)
admin.site.register(oficiales)