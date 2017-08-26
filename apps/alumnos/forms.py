from django import forms

from .models import AlumnoDatosPersonales, AlumnoDatosFisicos

class AlumnoDatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = AlumnoDatosPersonales
        fields = '__all__'

        widgets = {
            'boleta': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa    ó    dd/mm/aa    ó    aaaa-mm-dd'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5512345678'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'codigo_tarjeta': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        nombre = nombre.lower()

        return nombre

    def clean_apellido_paterno(self):
        apellido_paterno = self.cleaned_data.get("apellido_paterno")
        apellido_paterno = apellido_paterno.lower()

        return apellido_paterno

    def clean_apellido_materno(self):
        apellido_materno = self.cleaned_data.get("apellido_materno")
        apellido_materno = apellido_materno.lower()

        return apellido_materno

    def clean_edad(self):
        edad = self.cleaned_data.get("edad")

        if edad < 15 or edad > 80:
            raise forms.ValidationError("Escoge una edad entre 15 y 80")

        return edad

    def clean_codigo_tarjeta(self):
        codigo_tarjeta = self.cleaned_data.get("codigo_tarjeta")
        codigo_tarjeta = codigo_tarjeta.replace(' ', '')

        if len(codigo_tarjeta) < 8:
            raise forms.ValidationError("El código debe ser de 8 caracteres")

        codigo_tarjeta = codigo_tarjeta[:2] + " " + codigo_tarjeta[2:4] + " " + codigo_tarjeta[4:6] + " " + codigo_tarjeta[6:]
        codigo_tarjeta = codigo_tarjeta.upper()

        return codigo_tarjeta


class AlumnoDatosFisicosForm(forms.ModelForm):
    class Meta:
        model = AlumnoDatosFisicos
        fields = '__all__'

        labels = {
            'estatura': 'Estatura (m)',
            'peso': 'Peso (kg)',
            'circunferencia_cintura': 'Circunferencia de la cintura (cm)',
            'frecuencia_reposo': 'Frecuencia cardiaca en reposo (latidos/minuto)',
            'presion_arterial': 'Presion arterial (mm Hg)',
        }

        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-control'}),
            'estatura': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'circunferencia_cintura': forms.TextInput(attrs={'class': 'form-control'}),
            'frecuencia_reposo': forms.TextInput(attrs={'class': 'form-control'}),
            'presion_arterial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 120/80'}),
        }
