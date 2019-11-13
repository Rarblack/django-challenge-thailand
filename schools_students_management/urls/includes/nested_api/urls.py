from rest_framework_nested import routers
from django.conf.urls import include
from django.urls import path

from ....views.nested_api.student.views import StudentViewSet
from ....views.nested_api.school.views import SchoolViewSet

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)

schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentViewSet, base_name='school-students')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(schools_router.urls))
]