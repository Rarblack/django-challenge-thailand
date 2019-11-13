from rest_framework import generics
from django.shortcuts import get_object_or_404

from ....models.student.models import StudentModel
from ....models.school.models import SchoolModel
from ....serializers.student.serializers import StudentSerializer


class StudentsListCreateApiView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        school = get_object_or_404(
            SchoolModel, pk=request.data['school']
        )

        assert school.occupied_seats < school.capacity, 'No available seat'
        return self.create(request, *args, **kwargs)


class StudentRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer




