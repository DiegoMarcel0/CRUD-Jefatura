from django.urls import reverse, reverse_lazy
from django.views import generic
from ..models import oficiales, reportes_de_servicio
from ..forms import ReporteServicioForm, ReporteServicioUpdateForm, ReporteServicioDetailForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

#READ
class ReporteServicioView(generic.ListView):
    template_name = "comisaria/READ/reporteServicio.html"
    context_object_name ="reportes"
    def get_queryset(self):
        return reportes_de_servicio.objects.order_by("titulo")[:5]

#EDIT
class ReporteServicioUpdate(UpdateView):
    model = reportes_de_servicio
    form_class = ReporteServicioUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('reporte')
   
#DETALLES
class ReporteServicioDetallesView(generic.DetailView):
    model = reportes_de_servicio
    template_name = "comisaria/DETALLES/detalles.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReporteServicioDetailForm(instance=self.object)
        return context

#FORMS Creacion 
@login_required
def reporte_servicio_view(request):
    if request.method == "POST":
        form = ReporteServicioForm(request.POST)
        print(form.data)
        if form.is_valid():
            form = form.save(commit=False)
            form.num_placa = get_object_or_404(oficiales, pk = request.user.id)
            form.save()
            return HttpResponseRedirect(reverse("caso"))
        else:
            return render(request, 'comisaria/forms/form.html', {'form': form})
    form = ReporteServicioForm()
    return render(request, 'comisaria/forms/form.html', {'form': form})

#ELIMINAR
def reporte_servicio_delete_view(request, id):
    entidad = get_object_or_404(reportes_de_servicio, pk = id)
    entidad.delete()
    return HttpResponseRedirect(reverse('reporte_servicio'))

