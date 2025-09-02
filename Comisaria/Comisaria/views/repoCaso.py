from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from ..models import registro_casos, reportes_caso
from ..forms import ReporteCasoForm, ReporteCasoUpdateForm, ReporteCasoDetailForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

#READ
class ReporteCasoView(generic.ListView):
    template_name = "comisaria/READ/reportecaso.html"
    context_object_name ="reportes"
    def get_queryset(self):
        return reportes_caso.objects.order_by("titulo")[:5]
#EDIT
class ReporteCasoUpdate(UpdateView):
    model = reportes_caso
    form_class = ReporteCasoUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('caso')

#DETALLES
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
def reporte_caso_view(request, caso_id):
    if request.method == "POST":
        form = ReporteCasoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.id_caso = get_object_or_404(registro_casos, pk = caso_id)
            form.save()
            return HttpResponseRedirect(reverse('caso_deta', kwargs={'pk': caso_id}))
        else:
            return render(request, 'comisaria/forms/form.html', {'form': form})
    form = ReporteCasoForm()
    return render(request, 'comisaria/forms/form.html', {'form': form})

#ELIMINAR
def reporte_caso_delete_view(request,caso_id, id):
    entidad = get_object_or_404(reportes_caso, pk = id)
    entidad.delete()
    return HttpResponseRedirect(reverse('caso_deta', kwargs={'pk': caso_id}))