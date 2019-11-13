from django.urls import path

from schools_students_management.views.api.student import views


urlpatterns = []

urlpatterns += [
    path('students/', views.StudentsListCreateApiView.as_view(), name='list_create_student'),
    path('student/<int:pk>', views.StudentRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy_student'),
]
