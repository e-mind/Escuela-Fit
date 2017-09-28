from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.students.filters import AlumnoFilter

from .models import PhysicalRecord
from .forms import PhysicalRecordForm


class RecordCreate(CreateView):
    template_name = 'physical_record/form.html'
    form_class = PhysicalRecordForm
    success_url = reverse_lazy('record:list')

    def get_context_data(self, **kwargs):
        context = super(PhysicalRecordCreate, self).get_context_data(**kwargs)
        if self.kwargs['student']:
            student = self.kwargs['student'].replace('/', '')
            context['student'] = Student.objects.get(pk=student)
        return context

class RecordUpdate(UpdateView):
    model = PhysicalRecord
    template_name = 'physical_record/form.html'
    form_class = PhysicalRecordForm
    success_url = reverse_lazy('record:list')

    def get_context_data(self, **kwargs):
        context = super(PhysicalRecordUpdate, self).get_context_data(**kwargs)
        context['student'] = PhysicalRecord.objects.get(pk=self.kwargs['pk']).student
        return context

class RecordDetail(DetailView):
    model = PhysicalRecord
    template_name = 'physical_record/detail.html'

class RecordDelete(ListView):
    model = PhysicalRecord
    template_name = 'physical_record/delete.html'
    success_url = reverse_lazy('record:list')

def record_list(request):
    record_list = PhysicalRecord.objects.all()
    request.GET = request.GET.copy() # Devuelve un diccionario mutable
    for key, value in request.GET.items():
        request.GET[key] = value.lower()

    record_filter = AlumnoFilter(request.GET, queryset=record_list)
    paginator = Paginator(record_filter.qs, 5)

    page = request.GET.get('page')
    try:
        record = paginator.page(page)
    except PageNotAnInteger:
        record = paginator.page(1)
    except EmptyPage:
        record = paginator.page(paginator.num_pages)

    context = {
        'record': record,
    }
    return render(request, 'physical_record/list.html', context)
