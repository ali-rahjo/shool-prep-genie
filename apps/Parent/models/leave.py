from django.db import models
from apps.Parent.models import Parent  
from apps.Student.models import Student 
from django.utils import timezone



class Leave(models.Model):
    
    LEAVE_TYPE_CHOICES = [
        ('SICK', 'Sick Leave'),
        ('CASUAL', 'Casual Leave'),
        ('EMERGENCY', 'Emergency Leave'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    date = models.DateField(default=timezone.now, verbose_name="Date Sent")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    leave_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
   

    def __str__(self):
        return f"{self.student} - {self.leave_type} ({self.status})"
