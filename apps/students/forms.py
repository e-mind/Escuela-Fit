from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'student_number': forms.TextInput(attrs={'class': 'form-control'}),
            'career': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'second_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa    ó    dd/mm/aa    ó    aaaa-mm-dd'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5512345678'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'card_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        name = name.lower()

        return name

    def clean_first_surname(self):
        first_surname = self.cleaned_data.get("first_surname")
        first_surname = first_surname.lower()

        return first_surname

    def clean_second_surname(self):
        second_surname = self.cleaned_data.get("second_surname")
        second_surname = second_surname.lower()

        return second_surname

    def clean_age(self):
        age = self.cleaned_data.get("age")

        if age < 15 or age > 80:
            raise forms.ValidationError("Escoge una age entre 15 y 80")

        return age

    def clean_card_code(self):
        card_code = self.cleaned_data.get("card_code")
        card_code = card_code.replace(' ', '')

        if len(card_code) < 8:
            raise forms.ValidationError("El código debe ser de 8 caracteres")

        card_code = card_code[:2] + " " + card_code[2:4] + " " + card_code[4:6] + " " + card_code[6:]
        card_code = card_code.upper()

        return card_code


