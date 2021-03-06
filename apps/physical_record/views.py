from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from apps.students.models import Student
from apps.students.filters import StudentFilter

from .models import PhysicalRecord
from .forms import PhysicalRecordForm


class RecordCreate(CreateView):
    template_name = 'physical_record/form.html'
    form_class = PhysicalRecordForm
    success_url = reverse_lazy('record:list')

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'student': kwargs['student']})
        next = reverse_lazy('nutrition:create') if self.request.GET.get('next') == 'nutrition' else ''
        return render(request, self.template_name, {'form': form, 'next': next})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            redirect_to = request.POST.get('next', '')
            if redirect_to and is_safe_url(url=redirect_to, host=request.get_host()):
                return redirect(redirect_to)
            else:
                return redirect(reverse_lazy('record:list'))
        
        return render(request, self.template_name, {'form': form, 'next': request.POST.get('next','')})

class RecordUpdate(UpdateView):
    model = PhysicalRecord
    template_name = 'physical_record/form.html'
    form_class = PhysicalRecordForm
    success_url = reverse_lazy('record:list')

class RecordDelete(DeleteView):
    model = PhysicalRecord
    template_name = 'physical_record/delete.html'
    success_url = reverse_lazy('record:list')


@login_required
def record_list(request):
    if request.user.is_superuser:
        record_list = PhysicalRecord.objects.all()
        request.GET = request.GET.copy() # Devuelve un diccionario mutable
        for key, value in request.GET.items():
            request.GET[key] = value.lower()

        record_filter = StudentFilter(request.GET, queryset=record_list)
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
    else:
        record = PhysicalRecord.objects.filter(student=request.user.student)

        context = {
            'record': record,
        }


    return render(request, 'physical_record/list.html', context)
