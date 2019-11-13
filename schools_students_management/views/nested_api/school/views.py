from rest_framework import viewsets

from ....serializers.school.serializers import SchoolSerializer
from ....models.school.models import SchoolModel


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer

