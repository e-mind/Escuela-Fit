from django.contrib import admin

from .models import AlumnoDatosPersonales, AlumnoDatosFisicos

class AlumnoDatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ['boleta', 'email', 'nombre', 'apellido_paterno', 'apellido_materno', 'codigo_tarjeta']

class AlumnoDatosFisicosAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'fecha']

admin.site.register(AlumnoDatosPersonales, AlumnoDatosPersonalesAdmin)
admin.site.register(AlumnoDatosFisicos, AlumnoDatosFisicosAdmin)