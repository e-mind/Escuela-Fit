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

GENDER = (
    ('H', 'Hombre'),
    ('M', 'Mujer'),
)


class Student(models.Model):
    student_number = models.CharField("boleta", max_length=10, unique=True)
    career = models.CharField("carrera", max_length=2, choices=CAREERS)
    semester = models.CharField("semestre", max_length=1, choices=SEMESTERS)
    gender = models.CharField("género", max_length=1, choices=GENDER)
    name = models.CharField("nombre", max_length=30)
    first_surname = models.CharField("apellido paterno", max_length=30)
    second_surname = models.CharField("apellido materno", max_length=30)
    age = models.PositiveSmallIntegerField("edad")
    birthday = models.DateField("fecha de nacimiento")
    telephone = models.CharField("teléfono", max_length=10)
    email = models.EmailField("email", max_length=80)
    card_code = models.CharField("código tarjeta", max_length=11, null=True, blank=True)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.first_surname, self.second_surname)

    class Meta:
        ordering = ['first_surname', 'second_surname']
