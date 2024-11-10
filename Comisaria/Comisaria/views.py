from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import *#CustomUserCreationForm, CasosForm, OficialesForm, ReporteCasoForm, ReporteServicioForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView
from .models import *


"""def login(request):
    return render(request, 'comisaria/login.html')
"""
def index(request):
    return render(request, 'comisaria/index.html')

#READ
class EmpleadoView(generic.ListView):
    template_name = "comisaria/READ/empleado.html"
    context_object_name ="empleados"
    def get_queryset(self):
        return Empleado.objects.order_by("first_name")[:5]
    
class CasoView(generic.ListView):
    template_name = "comisaria/READ/caso.html"
    context_object_name ="casos"
    def get_queryset(self):
        return registro_casos.objects.order_by("titulo")[:5]
    
class OficialView(generic.ListView):
    template_name = "comisaria/READ/oficial.html"
    context_object_name ="oficiales"
    def get_queryset(self):
        return oficiales.objects.order_by("num_placa")[:5]

#EDIT
class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = CustomUserChangeForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('empleado')

class OficialUpdate(UpdateView):
    model = oficiales
    form_class = OficialesUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('oficial')
class CasoUpdate(UpdateView):
    model = registro_casos
    form_class = CasosForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('caso')
#DETALLES
class EmpleadoDetallesView2(generic.DetailView):
    model = Empleado
    template_name = "comisaria/DETALLES/detalles.html"
class EmpleadoDetallesView(UpdateView):
    model = Empleado
    form_class = EmpleadoDetail
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('empleado')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
        return form

class CasoDetallesView(generic.DetailView):
    model = registro_casos
    template_name = "comisaria/DETALLES/detalles.html"
class OficialDetallesView(generic.DetailView):
    model = oficiales
    template_name = "comisaria/DETALLES/detalles.html"
    
    
    #Empleado.last_name.verbose_name

#FORMS Creacion
@login_required
def empleado_form(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            if(request.POST["puesto"]==10):
                return HttpResponseRedirect(reverse("oficial_crear"))
            else:
                return HttpResponseRedirect(reverse("empleado"))
        else:
            message_error = "Formulario invalido"
    else:
        message_error = None
    form = CustomUserCreationForm()
    return render(request, 'comisaria/forms/form.html', {'form': form.as_p, 'error_message': message_error})


@login_required
def oficial_form(request):
    if request.method == "POST":
        form = OficialesForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("oficial"))
        else:
            message_error = "Formulario invalido"
    else:
        message_error = None
    form = OficialesForm()
    return render(request, 'comisaria/forms/form.html', {'form': form.as_p, 'error_message': message_error})
    #formu = OficialesForm()
    #print(formu.get_context)
    #return render(request, 'comisaria/empleado.html', {'form': formu.as_p})

@login_required
def caso_form(request):
    if request.method == "POST":
        form = CasosForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("caso"))
        else:
            message_error = "Formulario invalido"
    else:
        message_error = None
    form = CasosForm()
    return render(request, 'comisaria/forms/form.html', {'form': form.as_p, 'error_message': message_error})
    #formu = CasosForm()
    #print(formu.get_context)
    #return render(request, 'comisaria/empleado.html', {'form': formu.as_p})
@login_required
def reporte_caso_form(request):
    formu = ReporteCasoForm()
    #print(formu.get_context)
    return render(request, 'comisaria/empleado.html', {'form': formu.as_p})
@login_required
def reporte_servicio_form(request):
    formu = ReporteServicioForm()
    #print(formu.get_context)
    return render(request, 'comisaria/empleado.html', {'form': formu.as_p})
