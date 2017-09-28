from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'email', 'name', 'first_surname', 'second_surname', 'card_code']


admin.site.register(Student, StudentAdmin)
