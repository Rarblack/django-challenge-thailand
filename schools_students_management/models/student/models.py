import uuid
from django.db import models

from ..school.models import SchoolModel


class StudentModel(models.Model):

    first_name = models.CharField(
        max_length=20
    )

    last_name = models.CharField(
        max_length=20
    )

    identification_string = models.UUIDField(
        default=uuid.uuid4
    )

    school = models.ForeignKey(
        SchoolModel,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return '{0}: {1} {2}'.format(
            self.identification_string,
            self.first_name,
            self.last_name,
        )
