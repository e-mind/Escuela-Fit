from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .filters import AlumnoFilter
from .models import AlumnoDatosPersonales, AlumnoDatosFisicos
from .forms import AlumnoDatosPersonalesForm, AlumnoDatosFisicosForm

# DATOS PERSONALES
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

def alumno_list(request):
    alumno_list = AlumnoDatosPersonales.objects.all()
    request.GET = request.GET.copy() # Devuelve un diccionario mutable
    for key, value in request.GET.items():
        request.GET[key] = value.lower()

    alumno_filter = AlumnoFilter(request.GET, queryset=alumno_list)
    paginator = Paginator(alumno_filter.qs, 5)

    page = request.GET.get('page')
    try:
        alumnos = paginator.page(page)
    except PageNotAnInteger:
        alumnos = paginator.page(1)
    except EmptyPage:
        alumnos = paginator.page(paginator.num_pages)

    context = {
        'alumnos': alumnos,
        'filter': alumno_filter
    }

    return render(request, 'alumnos/list.html', context)


# DATOS FÍSICOS
class AlumnoFisicosCreate(CreateView):
    template_name = 'alumnos/fisicos/form.html'
    form_class = AlumnoDatosFisicosForm
    success_url = reverse_lazy('alumnos:list_fisicos')

    def get_context_data(self, **kwargs):
        context = super(AlumnoFisicosCreate, self).get_context_data(**kwargs)
        if self.kwargs['pk']:
            pk = self.kwargs['pk'].replace('/', '')
            context['alumno'] = AlumnoDatosPersonales.objects.get(pk=pk)
        return context

class AlumnoFisicosUpdate(UpdateView):
    model = AlumnoDatosFisicos
    template_name = 'alumnos/fisicos/form.html'
    form_class = AlumnoDatosFisicosForm
    success_url = reverse_lazy('alumnos:list_fisicos')

    def get_context_data(self, **kwargs):
        context = super(AlumnoFisicosUpdate, self).get_context_data(**kwargs)
        context['alumno'] = AlumnoDatosFisicos.objects.get(pk=self.kwargs['pk']).alumno
        return context

class AlumnoFisicosDetail(DetailView):
    model = AlumnoDatosFisicos
    template_name = 'alumnos/fisicos/detail.html'

class AlumnoFisicosDelete(ListView):
    model = AlumnoDatosFisicos
    template_name = 'alumnos/fisicos/delete.html'
    success_url = reverse_lazy('alumnos:list_fisicos')

def alumno_fisicos_list(request):
    alumno_list = AlumnoDatosFisicos.objects.all()
    request.GET = request.GET.copy() # Devuelve un diccionario mutable
    for key, value in request.GET.items():
        request.GET[key] = value.lower()

    alumno_filter = AlumnoFilter(request.GET, queryset=alumno_list)
    paginator = Paginator(alumno_filter.qs, 5)

    page = request.GET.get('page')
    try:
        alumnos = paginator.page(page)
    except PageNotAnInteger:
        alumnos = paginator.page(1)
    except EmptyPage:
        alumnos = paginator.page(paginator.num_pages)

    context = {
        'alumnos': alumnos,
    }
    return render(request, 'alumnos/fisicos/list.html', context)
