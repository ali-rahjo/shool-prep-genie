from django.core.validators import RegexValidator 
from django.db import models
from apps.Teacher.models.teacher import Teacher


class Parent(models.Model):
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d{9}$', message="Contact number should be 9 digits.")],
        blank=True,  
        null=True
    )
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')],blank=True, null=True, default='M')
    address = models.CharField(max_length=255, blank=True, null=True)   
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
   
    
    class Meta:
        verbose_name_plural = 'Parent'
        db_table = "parent"

        constraints = [
            
            models.UniqueConstraint(fields=['phone_number'], name='unique_contact_number'),
                
        ]

        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"




