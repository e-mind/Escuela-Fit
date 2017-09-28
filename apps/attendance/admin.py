from django.contrib import admin

from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'time']

admin.site.register(Attendance, AttendanceAdmin)
