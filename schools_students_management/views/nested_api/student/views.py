from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from ....serializers.student.serializers import StudentSerializer
from ....models.student.models import StudentModel
from ....models.school.models import SchoolModel


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return StudentModel.objects.filter(school=self.kwargs.get('school_pk'))

    def create(self, request, *args, **kwargs):
        # if there is no any place raise error
        school = get_object_or_404(
            SchoolModel, pk=request.data['school']
        )
        assert school.occupied_seats < school.capacity, 'No available seat'

        # else save as usual
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

