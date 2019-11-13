from django.contrib import admin

from schools_students_management.models.school.models import SchoolModel


@admin.register(SchoolModel)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity', 'occupied_seats']

