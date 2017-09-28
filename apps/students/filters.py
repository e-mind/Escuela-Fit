import django_filters

from .models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['student_number', 'name', 'first_surname', 'second_surname']