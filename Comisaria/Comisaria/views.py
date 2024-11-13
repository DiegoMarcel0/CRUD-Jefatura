from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
class ReporteCasoView(generic.ListView):
    template_name = "comisaria/READ/reportecaso.html"
    context_object_name ="reportes"
    def get_queryset(self):
        return reportes_caso.objects.order_by("titulo")[:5]
    
class ReporteServicioView(generic.ListView):
    template_name = "comisaria/READ/reporteServicio.html"
    context_object_name ="reportes"
    def get_queryset(self):
        return reportes_de_servicio.objects.order_by("titulo")[:5]

#EDIT
class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('empleado')

class OficialUpdate(UpdateView):
    model = oficiales
    form_class = OficialesUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('oficial')
class CasoUpdate(UpdateView):
    model = registro_casos
    form_class = CasoUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('caso')
class ReporteServicioUpdate(UpdateView):
    model = reportes_de_servicio
    form_class = ReporteServicioUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('reporte')
class ReporteCasoUpdate(UpdateView):
    model = reportes_caso
    form_class = ReporteCasoUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('caso')
#DETALLES
class EmpleadoDetallesView(generic.DetailView):
    model = Empleado
    template_name = "comisaria/DETALLES/detalles.html"
    context_object_name="empleado"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmpleadoDetailForm(instance=self.object)
        return context

class CasoDetallesView(generic.DetailView):
    model = registro_casos
    template_name = "comisaria/DETALLES/detallesCaso.html"
    context_object_name = 'caso'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CasosDetailForm(instance=self.object)
        return context
class OficialDetallesView(generic.DetailView):
    model = oficiales
    template_name = "comisaria/DETALLES/detalles.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OficialDetailForm(instance=self.object)
        return context
class ReporteServicioDetallesView(generic.DetailView):
    model = reportes_de_servicio
    template_name = "comisaria/DETALLES/detalles.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReporteServicioDetailForm(instance=self.object)
        return context
class ReporteCasoDetallesView(generic.DetailView):
    model = reportes_caso
    template_name = "comisaria/DETALLES/detalles.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Instanciar el formulario con la instancia del producto
        context['form'] = ReporteCasoDetailForm(instance=self.object)
        return context

#FORMS Creacion
@login_required
def empleado_view(request):
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
    return render(request, 'comisaria/forms/form.html', {'form': form, 'error_message': message_error})


@login_required
def oficial_view(request):
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
    return render(request, 'comisaria/forms/form.html', {'form': form, 'error_message': message_error})

@login_required
def caso_view(request):
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
    return render(request, 'comisaria/forms/form.html', {'form': form, 'error_message': message_error})
@login_required
def reporte_caso_view(request, caso_id):
    #reporte = get_object_or_404(registro_casos, pk = caso_id)
    if request.method == "POST":
        form = ReporteCasoForm(request.POST)
        #print(form.cleaned_data)
        #form.id_caso = caso_id
        #print(form.data)
        #print(form.data)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.id_caso = get_object_or_404(registro_casos, pk = caso_id)
            form.save()
            return HttpResponseRedirect(reverse("caso"))
        else:
            message_error = "Formulario invalido"
            print(message_error)
    else:
        message_error = None
    form = ReporteCasoForm()
    return render(request, 'comisaria/forms/form.html', {'form': form, 'error_message': message_error})
@login_required
def reporte_servicio_view(request):
    if request.method == "POST":
        form = ReporteServicioForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("caso"))
        else:
            message_error = "Formulario invalido"
    else:
        message_error = None
    form = ReporteServicioForm()
    return render(request, 'comisaria/forms/form.html', {'form': form, 'error_message': message_error})
