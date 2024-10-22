from django.db import models


class Teacher(models.Model):

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



class Class(models.Model):
    class_name = models.CharField(max_length=100)
    academic_year_start = models.IntegerField()
    academic_year_end = models.IntegerField()
    grade = models.IntegerField()
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
   

    def __str__(self):
        return f"Class:{self.class_name} (Grade: {self.grade}, ID: {self.id})"