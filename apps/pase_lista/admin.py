from django.contrib import admin

from .models import Asistencia

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'fecha', 'hora']

admin.site.register(Asistencia, AsistenciaAdmin)
