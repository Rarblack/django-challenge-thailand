from django.conf.urls import include
from django.urls import path

urlpatterns = []

# API
urlpatterns += [
    path('', include('schools_students_management.urls.includes.api.school.urls')),
    path('', include('schools_students_management.urls.includes.api.student.urls')),
]

# NESTED API
urlpatterns += [
    path('', include('schools_students_management.urls.includes.nested_api.urls')),
]