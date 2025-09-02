from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from ..models import registro_casos
from ..forms import CasoUpdateForm, CasosDetailForm, CasosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

#READ
class CasoView(generic.ListView):
    template_name = "comisaria/READ/caso.html"
    context_object_name ="casos"
    def get_queryset(self):
        return registro_casos.objects.order_by("titulo")[:5]
    
#EDIT
class CasoUpdate(UpdateView):
    model = registro_casos
    form_class = CasoUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('caso')

#DETALLES
class CasoDetallesView(generic.DetailView):
    model = registro_casos
    template_name = "comisaria/DETALLES/detallesCaso.html"
    context_object_name = 'caso'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CasosDetailForm(instance=self.object)
        return context
#FORMS Creacion
@login_required
def caso_view(request):
    if request.method == "POST":
        form = CasosForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("caso"))
        else:
            return render(request, 'comisaria/forms/form.html', {'form': form})
    form = CasosForm()
    return render(request, 'comisaria/forms/form.html', {'form': form})

#ELIMINAR
def caso_delete_view(request, id):
    entidad = get_object_or_404(registro_casos, pk = id)
    entidad.delete()
    return HttpResponseRedirect(reverse('caso'))