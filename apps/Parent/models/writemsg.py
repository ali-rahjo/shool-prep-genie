from django.db import models
from apps.Parent.models.parent import Parent  
from apps.Student.models.student import Student 
from django.utils import timezone



class WriteMsg(models.Model):
    
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="Sender Parent")  
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student Involved")
    text_msg = models.TextField(verbose_name="Message Text")
    response = models.TextField(verbose_name="Teacher Response", blank=True, null=True)
    date = models.DateField(default=timezone.now, verbose_name="Date Sent")

    def __str__(self):
        return f"Message from {self.parent}  for {self.student} "
