from django.urls import reverse, reverse_lazy
from django.views import generic
from ..models import Empleado
from ..forms import EmpleadoUpdateForm, EmpleadoDetailForm, CustomUserCreationForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

#READ
class EmpleadoView(generic.ListView):
    template_name = "comisaria/READ/empleado.html"
    context_object_name ="empleados"
    def get_queryset(self):
        return Empleado.objects.order_by("first_name")[:5]
    
#EDIT
class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoUpdateForm
    template_name = 'comisaria/forms/form.html'
    success_url = reverse_lazy('empleado')

#DETALLES
class EmpleadoDetallesView(generic.DetailView):
    model = Empleado
    template_name = "comisaria/DETALLES/detalles.html"
    context_object_name="empleado"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmpleadoDetailForm(instance=self.object)
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
            return render(request, 'comisaria/forms/form.html', {'form': form})
    form = CustomUserCreationForm()
    return render(request, 'comisaria/forms/form.html', {'form': form})

#ELIMINAR
def empleado_delete_view(request, id):
    entidad = get_object_or_404(Empleado, pk = id)
    entidad.delete()
    return HttpResponseRedirect(reverse('empleado'))
