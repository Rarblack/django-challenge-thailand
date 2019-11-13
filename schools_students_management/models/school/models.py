from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class SchoolModel(models.Model):

    name = models.CharField(
        max_length=20
    )

    capacity = models.IntegerField()

    occupied_seats = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @receiver(post_save, sender='schools_students_management.StudentModel')
    def update_availability(sender, instance, created, **kwargs):
        if created:
            instance.school.occupied_seats += 1
            instance.school.save()



