from django.urls import path
from .....views.api.school import views
urlpatterns = []

urlpatterns += [
    path('schools/', views.SchoolsListCreateApiView.as_view(), name='list_create_school'),
    path('school/<int:pk>', views.SchoolRetrieveUpdateDestroyApiView.as_view(), name='retrieve_update_destroy_school'),
]