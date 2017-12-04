from django.db import models

from apps.students.models import Student


class PhysicalRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="alumno")
    height = models.FloatField("estatura", max_length=4)
    weight = models.FloatField("peso", max_length=7)
    waist_circumference = models.FloatField("circunferencia de la cintura", max_length=7, blank=True, null=True)
    resting_heart_rate = models.IntegerField("frecuencia cardiaca en reposo", blank=True, null=True)
    blood_pressure = models.CharField("presión arterial", max_length=7, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.student, self.date)

    class Meta:
        ordering = ['-date']
