from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Announcement(models.Model):
    date = models.DateField(default=date.today)
    announcement = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"DATE: {self.date}, ANNOUNCEMENT: {self.announcement}"
