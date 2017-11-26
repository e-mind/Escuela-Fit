from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Student
from .forms import StudentForm
from .filters import StudentFilter

class StudentCreate(CreateView):
    template_name = 'students/form.html'
    form_class = StudentForm

    def get(self, request):
        if hasattr(request.user, 'student'):
            pk = request.user.student.pk
            return redirect(reverse_lazy('students:detail', kwargs={'pk': pk}))

        return super(StudentCreate, self).get(request)

    def form_valid(self, form):
        student = form.save()
        self.request.user.first_name = student.name
        self.request.user.last_name = student.first_surname
        student.user = self.request.user
        self.request.user.save()
        student.save()
        return redirect(reverse_lazy('students:detail', kwargs={'pk': student.pk}))

class StudentUpdate(UpdateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm

    def form_valid(self, form):
        student = form.save()
        return redirect(reverse_lazy('students:detail', kwargs={'pk': student.pk}))

class StudentDetail(DetailView):
    model = Student
    template_name = 'students/detail.html'

class StudentDelete(DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')

@login_required
def student_list(request):
    if request.user.is_superuser:
        student_list = Student.objects.all()
        request.GET = request.GET.copy()
        for key, value in request.GET.items():
            request.GET[key] = value.lower()

        student_filter = StudentFilter(request.GET, queryset=student_list)
        paginator = Paginator(student_filter.qs, 5)

        page = request.GET.get('page')
        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)

        context = {
            'students': students,
            'filter': student_filter
        }

        return render(request, 'students/list.html', context)
    else:
        return HttpResponse(request.user.id)
