from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'career', 'semester', 'gender', 'name', 'first_surname', 'second_surname', 'age', 'birthday', 'telephone', 'email', 'card_code']

        widgets = {
            'age': forms.NumberInput(attrs={'min': '15', 'max': '70'}),
            'birthday': forms.DateInput(attrs={'type': 'date'},  format='%Y-%m-%d'),
            'telephone': forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Ej. 5512345678'}),
        }

    def clean_student_number(self):
        student_number = self.cleaned_data.get("student_number")

        if len(student_number) != 10:
            raise forms.ValidationError("Escribe una boleta válida. Ej: 2016609999")

        return student_number

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

        if age < 15 or age > 70:
            raise forms.ValidationError("Escoge una age entre 15 y 70")

        return age

    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        telephone = telephone.replace(" ", "")
        telephone = telephone.replace("-", "")
        telephone = telephone.replace(".", "")
        telephone = telephone.replace("(", "")
        telephone = telephone.replace(")", "")

        if len(telephone) not in [8,10]:
            raise forms.ValidationError("Escribe un formato válido. Ej: 5512345678")

        return telephone

    def clean_card_code(self):
        card_code = self.cleaned_data.get("card_code")
        if card_code:
            card_code = card_code.replace(' ', '')

            if len(card_code) != 8:
                raise forms.ValidationError("El código debe ser de 8 caracteres")

            card_code = card_code[:2] + " " + card_code[2:4] + " " + card_code[4:6] + " " + card_code[6:]
            card_code = card_code.upper()

            return card_code
        else:
            return None
