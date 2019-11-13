from rest_framework import serializers

from ...models.school.models import SchoolModel


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolModel
        fields = '__all__'
