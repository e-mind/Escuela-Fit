from django.db import models

from apps.students.models import Student


class PhysicalRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    height = models.CharField("Estatura", max_length=4, blank=True, null=True)
    weight = models.CharField("Peso", max_length=7, blank=True, null=True)
    waist_circumference = models.CharField("Circunferencia de la cintura", max_length=7, blank=True, null=True)
    resting_heart_rate = models.CharField("Frecuencia cardiaca en reposo", max_length=7, blank=True, null=True)
    blood_pressure = models.CharField("Presión arterial", max_length=7, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.student, self.date)

    class Meta:
        ordering = ['-date']
