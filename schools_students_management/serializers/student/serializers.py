from rest_framework import serializers

from ...models.student.models import StudentModel


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        exclude = ['identification_string']
