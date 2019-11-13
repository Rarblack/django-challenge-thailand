from django.contrib import admin

from schools_students_management.models.student.models import StudentModel


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name', 'get_school_name']

    def get_full_name(self, instance):
        return f'{instance.first_name} {instance.last_name}'
    get_full_name.short_description = 'Full Name'

    def get_school_name(self, instance):
        return instance.school.name
    get_school_name.short_description = 'School'


