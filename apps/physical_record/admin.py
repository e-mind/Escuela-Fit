from django.contrib import admin

from .models import PhysicalRecord


class PhysicalRecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'date']


admin.site.register(PhysicalRecord, PhysicalRecordAdmin)
