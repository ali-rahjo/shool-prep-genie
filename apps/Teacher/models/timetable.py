from django.db import models
from apps.Teacher.models import Teacher
from apps.Teacher.models.teacher import Class

class TimeTable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.PROTECT)
    timetable_content = models.JSONField()

    def __str__(self):
        return f"Timetable for {self.class_id}"
    class Meta:
        unique_together = ('teacher', 'class_id') 