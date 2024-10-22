from django.db import models

# from apps.Student.models.student import Student
from apps.Teacher.models.teacher import Teacher
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class Attendance(models.Model):

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(
        "Student.Student", related_name="student", on_delete=models.CASCADE, default=1
    )
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=True)

    class Meta:
            unique_together = ('student', 'date') 

    def clean(self):

        if self.date > timezone.now().date():
            raise ValidationError("Attendance cannot be marked for future dates.")

    def __str__(self):
        return f"{self.date} --> {self.student} --> {'Present' if self.is_present else 'Absent'}"
