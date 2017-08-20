import django_filters

from .models import AlumnoDatosPersonales


class AlumnoFilter(django_filters.FilterSet):
    class Meta:
        model = AlumnoDatosPersonales
        fields = ['boleta', 'nombre', 'apellido_paterno', 'apellido_materno']