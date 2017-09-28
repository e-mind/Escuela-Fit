from django import forms

from .models import PhysicalRecord


class PhysicalRecordForm(forms.ModelForm):
    class Meta:
        model = PhysicalRecord
        fields = '__all__'

        labels = {
            'height': 'Estatura (m)',
            'weight': 'Peso (kg)',
            'waist_circumference': 'Circunferencia de la cintura (cm)',
            'resting_heart_rate': 'Frecuencia cardiaca en reposo (latidos/minuto)',
            'blood_pressure': 'Presion arterial (mm Hg)',
        }

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'waist_circumference': forms.TextInput(attrs={'class': 'form-control'}),
            'resting_heart_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_pressure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 120/80'}),
        }
