from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .filters import AlumnoFilter
from .models import AlumnoDatosPersonales, AlumnoDatosFisicos
from .forms import AlumnoDatosPersonalesForm, AlumnoDatosFisicosForm


class AlumnoCreate(CreateView):
    template_name = 'alumnos/form.html'
    form_class = AlumnoDatosPersonalesForm
    success_url = reverse_lazy('alumnos:list')

class AlumnoUpdate(UpdateView):
    model = AlumnoDatosPersonales
    template_name = 'alumnos/form.html'
    form_class = AlumnoDatosPersonalesForm
    success_url = reverse_lazy('alumnos:list')

class AlumnoDetail(DetailView):
    model = AlumnoDatosPersonales
    template_name = 'alumnos/detail.html'

class AlumnoDelete(DeleteView):
    model = AlumnoDatosPersonales
    template_name = 'alumnos/delete.html'
    success_url = reverse_lazy('alumnos:list')

def alumnoList(request):
    alumno_list = AlumnoDatosPersonales.objects.all()
    request.GET = request.GET.copy() # Devuelve un diccionario mutable
    for key, value in request.GET.items():
        request.GET[key] = value.lower()

    alumno_filter = AlumnoFilter(request.GET, queryset=alumno_list)
    paginator = Paginator(alumno_filter.qs, 2)

    page = request.GET.get('page')
    try:
        alumnos = paginator.page(page)
    except PageNotAnInteger:
        alumnos = paginator.page(1)
    except EmptyPage:
        alumnos = paginator.page(paginator.num_pages)

    return render(request, 'alumnos/list.html', {'alumnos': alumnos, 'filter': alumno_filter})