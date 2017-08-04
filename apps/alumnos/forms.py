from django import forms

from .models import Alumno

class AlumnoModelForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

        widgets = {
            'boleta': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'estatura': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'circunferencia_cintura': forms.TextInput(attrs={'class': 'form-control'}),
            'frecuencia_reposo': forms.TextInput(attrs={'class': 'form-control'}),
            'presion_arterial': forms.TextInput(attrs={'class': 'form-control'}),
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
