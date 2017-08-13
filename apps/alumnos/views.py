from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class AlumnoList(ListView):
    model = AlumnoDatosPersonales
    template_name = 'alumnos/list.html'

class AlumnoDetail(DetailView):
    model = AlumnoDatosPersonales
    template_name = 'alumnos/detail.html'

class AlumnoDelete(DeleteView):
    model = AlumnoDatosPersonales
    template_name = 'alumnos/delete.html'
    success_url = reverse_lazy('alumnos:list')