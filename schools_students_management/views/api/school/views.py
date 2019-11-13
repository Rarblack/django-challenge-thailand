from rest_framework import generics

from ....models.school.models import SchoolModel
from ....serializers.school.serializers import SchoolSerializer


class SchoolsListCreateApiView(generics.ListCreateAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer


class SchoolRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer




