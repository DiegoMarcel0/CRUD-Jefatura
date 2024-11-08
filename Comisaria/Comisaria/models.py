from django.db import models
from django.utils import timezone
import uuid
import random
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser

class Empleado(AbstractUser):
    first_name = models.CharField(max_length=50, default='', blank=False, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=50, default='', blank=False, verbose_name='Apellido paterno')
    last_name2 = models.CharField(max_length=50, default='', blank=False, verbose_name='Apellido materno')
    email = models.EmailField(unique=True, verbose_name='Correo')
    puesto = models.CharField(max_length=30, default='', blank=False, verbose_name='Puesto')
    register_date = models.DateTimeField(default= timezone.now, null=True, blank=False, verbose_name='Fecha de registro')
    num_phone = models.CharField(max_length=14, default='', blank=False, verbose_name='Telefono')
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    def save(self, *args, **kwargs):
        self.username = "{}{}{}".format(self.first_name.split()[0] if self.first_name.strip() else "", 
                                        self.last_name, 
                                        ''.join(map(str, random.sample(range(10), 4)))  )
        super().save(*args, **kwargs)

"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    first_name = models.CharField(max_length=50, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=50, verbose_name='Apellido(s)')
    email = models.EmailField(unique=True, verbose_name='Correo')
    puesto = models.CharField(max_length=30, verbose_name='Puesto')
    register_date = models.DateTimeField(default= timezone.now(), verbose_name='Fecha de registro')
    num_phone = models.CharField(max_length=14, verbose_name='Telefono')
"""
"""
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
"""
"""
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

"""


class oficiales(models.Model):
    num_placa = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Numero de placa')
    id_emp = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name='ID empleado')
    rank = models.CharField(max_length=21, verbose_name='Rango')
    def __str__(self):
        return f'{self.num_placa} {self.rank}'
    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales'


class reportes_de_servicio(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    contenido = models.TextField(verbose_name='Contenido')
    num_placa = models.ForeignKey(oficiales, on_delete=models.CASCADE, verbose_name='Oficial')
    tipo = models.CharField(max_length=20, verbose_name='Tipo de reporte')
    fecha = models.DateField(auto_now=False, verbose_name='Fecha de Reporte')
    class Meta:
        verbose_name = 'Reporte de servicio'
        verbose_name_plural = 'Reportes de servicio'

    def __str__(self):
        return f'{self.titulo}'
    

class registro_casos(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripcion')
    num_placa = models.ForeignKey(oficiales, on_delete=models.CASCADE, verbose_name='Designado')
    estatus = models.CharField(max_length=20, verbose_name='Estatus')
    fecha_inicio = models.DateField(auto_now=False, verbose_name='Fecha de Regsitro')
    fecha_fin = models.DateField(auto_now=False , null=True, blank=True, verbose_name='Fecha de cerrado')
    class Meta:
        verbose_name = 'Registro de caso'
        verbose_name_plural = 'Registros de Casos'

    def __str__(self):
        return f'{self.titulo} {self.estatus}'

class reportes_caso(models.Model):
    id_caso= models.ForeignKey(registro_casos, on_delete=models.CASCADE, verbose_name='Caso')
    fecha_reporte = models.DateTimeField(verbose_name='Fecha de reporte')
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    contenido = models.TextField(verbose_name='Contenido')
    tipo = models.CharField(max_length=20, verbose_name='Tipo')
    class Meta:
        verbose_name = 'Reporte de caso'
        verbose_name_plural = 'Reportes de casos'

    def __str__(self):
        return f'{self.titulo}'


    