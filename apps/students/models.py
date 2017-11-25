from django.db import models
from django.contrib.auth.models import User


CAREERS = (
    ('AI', 'Administración Industrial'),
    ('II', 'Ingeniería Industrial'),
    ('IT', 'Ingeniería en Transporte'),
    ('IN', 'Ingeniería en Informática'),
    ('CI', 'Ciencias de la Informática'),
)

SEMESTERS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)


class Student(models.Model):
    student_number = models.CharField("Boleta", max_length=10, unique=True)
    career = models.CharField("Carrera", max_length=2, choices=CAREERS)
    semester = models.CharField("Semestre", max_length=1, choices=SEMESTERS)
    name = models.CharField("Nombre", max_length=30)
    first_surname = models.CharField("Apellido Paterno", max_length=30)
    second_surname = models.CharField("Apellido Materno", max_length=30)
    age = models.PositiveSmallIntegerField("Edad")
    birthday = models.DateField("Fecha de nacimiento")
    telephone = models.CharField("Teléfono", max_length=10)
    email = models.EmailField("Email", max_length=80)
    card_code = models.CharField("Código Tarjeta", max_length=11)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.first_surname, self.second_surname)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('students:detail', args=[str(self.id)])

    class Meta:
        ordering = ['first_surname', 'second_surname']
