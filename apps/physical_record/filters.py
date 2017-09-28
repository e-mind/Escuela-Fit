import django_filters

from .models import PhysicalRecord


class PhysicalRecordFilter(django_filters.FilterSet):
    class Meta:
        model = PhysicalRecord
        fields = ['date', 'student']