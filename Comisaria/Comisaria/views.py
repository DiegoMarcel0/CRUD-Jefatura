from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *#CustomUserCreationForm, CasosForm, OficialesForm, ReporteCasoForm, ReporteServicioForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import *


"""def login(request):
    return render(request, 'comisaria/login.html')
"""
def index(request):
    return render(request, 'comisaria/index.html')

class empleadoView(generic.ListView):
    template_name = "comisaria/empleado.html"
    context_object_name ="empleados"
    def get_queryset(self):
        return Empleado.objects.order_by("first_name")[:5]

class empleadoDetallesView(generic.DetailView):
    model = Empleado
    template_name = "comisaria/detalles.html"

#Forms Creacion
@login_required
def empleado_form(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("inicio"))
        else:
            message_error = "Formulario invalido"
    else:
        message_error = None
    form = CustomUserCreationForm()
    return render(request, 'comisaria/forms/form.html', {'form': form.as_p, 'error_message': message_error})


@login_required
def oficial_form(request):
    formu = OficialesForm()
    #print(formu.get_context)
    return render(request, 'comisaria/empleado.html', {'form': formu.as_p})
@login_required
def caso_form(request):
    formu = CasosForm()
    #print(formu.get_context)
    return render(request, 'comisaria/empleado.html', {'form': formu.as_p})
@login_required
def reporteCaso_form(request):
    formu = ReporteCasoForm()
    #print(formu.get_context)
    return render(request, 'comisaria/empleado.html', {'form': formu.as_p})
@login_required
def reporteServicio_form(request):
    formu = ReporteServicioForm()
    #print(formu.get_context)
    return render(request, 'comisaria/empleado.html', {'form': formu.as_p})
