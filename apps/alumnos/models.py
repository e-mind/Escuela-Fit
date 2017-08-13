from django.db import models

CARRERAS = (
    ('AI', 'Administración Industrial'),
    ('II', 'Ingeniería Industrial'),
    ('IT', 'Ingeniería en Transporte'),
    ('IN', 'Ingeniería en Informática'),
    ('CI', 'Ciencias de la Informática'),
)

SEMESTRES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)


class AlumnoDatosPersonales(models.Model):
    boleta = models.CharField("Boleta", max_length=10, unique=True)
    carrera = models.CharField("Carrera", max_length=2, choices=CARRERAS)
    semestre = models.CharField("Semestre", max_length=1, choices=SEMESTRES)
    nombre = models.CharField("Nombre", max_length=30)
    apellido_paterno = models.CharField("Apellido Paterno", max_length=30)
    apellido_materno = models.CharField("Apellido Materno", max_length=30)
    edad = models.PositiveSmallIntegerField("Edad")
    fecha_nacimiento = models.DateField("Fecha de nacimiento")
    telefono = models.CharField("Teléfono", max_length=10)
    email = models.EmailField("Email", max_length=80)
    codigo_tarjeta = models.CharField("Código Tarjeta", max_length=11)

    class Meta:
        ordering = ['apellido_paterno']


class AlumnoDatosFisicos(models.Model):
    alumno = models.ForeignKey(AlumnoDatosPersonales, on_delete=models.CASCADE)
    estatura = models.CharField("Estatura", max_length=4, blank=True, null=True)
    peso = models.CharField("Peso", max_length=7, blank=True, null=True)
    circunferencia_cintura = models.CharField("Circunferencia de la cintura", max_length=7, blank=True, null=True)
    frecuencia_reposo = models.CharField("Frecuencia cardiaca en reposo", max_length=7, blank=True, null=True)
    presion_arterial = models.CharField("Presión arterial", max_length=7, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['fecha']
