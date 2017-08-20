from django.db import models

from apps.alumnos.models import AlumnoDatosPersonales


class Asistencia(models.Model):
    alumno = models.ForeignKey(AlumnoDatosPersonales, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.fecha, self.hora)

    class Meta:
        ordering = ['-fecha']
        