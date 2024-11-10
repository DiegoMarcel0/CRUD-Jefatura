from django.db import models
from django.utils import timezone
import uuid
import random
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser

class Empleado(AbstractUser):
    class Puesto(models.IntegerChoices):
        ADMINISTRATIVO = 1, "Personal Administrativo"
        INTELIGENCIA = 2, "Analistas de Inteligencia"
        FORENSE = 3, "Técnico Forense"
        ARCHIVO = 4, "Personal del Archivo"
        COMUNICACION = 5, "Operador de Comunicación"
        PSICOLOGIA = 6, "Psicólogos"
        MANTENIMIENTO = 7, "Personal de Mantenimiento"
        HUMANOS = 8, "Encargado de Recursos Humanos"
        TI = 9, "Tecnicos de Sistemas Informaticos"
        OFICIAL = 10, "Oficial"
    first_name = models.CharField(max_length=50, default='', blank=False, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=50, default='', blank=False, verbose_name='Apellido paterno')
    last_name2 = models.CharField(max_length=50, default='', blank=False, verbose_name='Apellido materno')
    email = models.EmailField(unique=True, verbose_name='Correo')
    puesto = models.IntegerField(choices=Puesto.choices, default=Puesto.ADMINISTRATIVO, verbose_name='Puesto')
    #puesto = models.CharField(max_length=30, default='', blank=False, verbose_name='Puesto')
    register_date = models.DateTimeField(default= timezone.now, null=True, blank=False, verbose_name='Fecha de registro')
    num_phone = models.CharField(max_length=14, default='', blank=False, verbose_name='Telefono')
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    def save(self, *args, **kwargs):
        print(self.username)
        if (self.username== None or self.username==""):
            self.username = "{}{}{}".format(self.first_name.split()[0] if self.first_name.strip() else "", 
                                            self.last_name.split()[0] if self.first_name.strip() else "",
                                            ''.join(map(str, random.sample(range(10), 4)))
                                            )
        super().save(*args, **kwargs)




class oficiales(models.Model):
    #num_placa = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Numero de placa')
    class Rango(models.IntegerChoices):
        POLICIA = 1, "Policía"
        INSPECTOR = 2, "Inspector"
        COMISARIO = 3, "Comisario"
    num_placa = models.PositiveIntegerField(default=0,blank=True, verbose_name='Numero de placa')
    id_emp = models.OneToOneField(Empleado, on_delete=models.CASCADE, verbose_name='ID empleado')
    rank = models.IntegerField(choices=Rango.choices, default=Rango.POLICIA, verbose_name='Rango')
    #rank = models.CharField(max_length=21, verbose_name='Rango')
    def __str__(self):
        return f'{self.num_placa}'
    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales'
    def save(self, *args, **kwargs):
        if (self.num_placa== None or self.num_placa==0):
            self.num_placa = "{}".format(''.join(map(str, random.sample(range(10), 5))))
        super().save(*args, **kwargs)


class reportes_de_servicio(models.Model):
    class Tipo(models.IntegerChoices):
        PATRULLAJE = 1, "Patrullaje"
        INCIDENTE = 2, "Incidente"
        ARRESTO = 3, "Arresto"
        TRAFICO = 4, "Tráfico o colisión"
        DIARIA = 5, "Actividad diaria"
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    contenido = models.TextField(verbose_name='Contenido')
    num_placa = models.ForeignKey(oficiales, on_delete=models.CASCADE, verbose_name='Oficial')
    tipo = models.IntegerField(choices=Tipo.choices, default=Tipo.DIARIA, verbose_name='Tipo de reporte')
    #tipo = models.CharField(max_length=20, verbose_name='Tipo de reporte')
    fecha = models.DateField(auto_now=False, verbose_name='Fecha de Reporte')
    class Meta:
        verbose_name = 'Reporte de servicio'
        verbose_name_plural = 'Reportes de servicio'
    def __str__(self):
        return f'{self.titulo}'
    

class registro_casos(models.Model):
    class Estatus(models.IntegerChoices):
        ABIERTO = 1, "Abierto"
        CERRADO = 2, "Cerrado"
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripcion')
    num_placa = models.ForeignKey(oficiales, on_delete=models.CASCADE, verbose_name='Designado')
    #estatus = models.CharField(max_length=20, verbose_name='Estatus')
    estatus = models.IntegerField(choices=Estatus.choices, default=Estatus.ABIERTO, verbose_name='Estatus')
    fecha_inicio = models.DateField(auto_now=False, verbose_name='Fecha de Regsitro')
    fecha_fin = models.DateField(auto_now=False , null=True, blank=True, verbose_name='Fecha de cerrado')
    class Meta:
        verbose_name = 'Registro de caso'
        verbose_name_plural = 'Registros de Casos'
    def __str__(self):
        return f'{self.titulo} {self.estatus}'

class reportes_caso(models.Model):
    class Tipo(models.IntegerChoices):
        INICIAL = 1, "Investigacion inicial"
        ENTREVISTA = 2, "Entrevista o Interrogatorio"
        EVIDENCIA = 3, "Evidencias"
        PERICIAL = 4, "Pericial forense"
        INTELIGENCIA = 5, "De inteligencia"
        VIGILANCIA = 6, "Observación o vigilancia"
    id_caso= models.ForeignKey(registro_casos, on_delete=models.CASCADE, verbose_name='Caso')
    fecha_reporte = models.DateTimeField(verbose_name='Fecha de reporte')
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    contenido = models.TextField(verbose_name='Contenido')
    #tipo = models.CharField(max_length=20, verbose_name='Tipo de reporte')
    tipo = models.IntegerField(choices=Tipo.choices, default=Tipo.INICIAL, verbose_name='Tipo de reporte')
    class Meta:
        verbose_name = 'Reporte de caso'
        verbose_name_plural = 'Reportes de casos'

    def __str__(self):
        return f'{self.titulo} {self.tipo}'


    