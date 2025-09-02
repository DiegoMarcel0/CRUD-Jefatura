from django.urls import reverse, reverse_lazy
from django.views import generic
from ..models import oficiales
from ..forms import OficialesForm, OficialesUpdateForm, OficialDetailForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

#READ
class OficialView(generic.ListView):
    template_name = "comisaria/READ/oficial.html"
    context_object_name ="oficiales"
    def get_queryset(self):
        return oficiales.objects.order_by("num_placa")[:5]

#EDIT
class OficialUpdate(UpdateView):
    model = oficiales
    form_class = OficialesUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('oficial')

#DETALLES
class OficialDetallesView(generic.DetailView):
    model = oficiales
    template_name = "comisaria/DETALLES/detalles.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OficialDetailForm(instance=self.object)
        return context

#FORMS Creacion
@login_required
def oficial_view(request):
    if request.method == "POST":
        form = OficialesForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("oficial"))
        else:
            return render(request, 'comisaria/forms/form.html', {'form': form})
    form = OficialesForm()
    return render(request, 'comisaria/forms/form.html', {'form': form})

#ELIMINAR
def oficial_delete_view(request, id):
    entidad = get_object_or_404(oficiales, pk = id)
    entidad.delete()
    return HttpResponseRedirect(reverse('oficial'))
