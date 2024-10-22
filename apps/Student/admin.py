from django.contrib import admin
from apps.Student.models.student import Student



class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'username',
        'age',
        'gender',
        'class_name',
        'parent_full_name',
        'teacher_name'
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Student Name'

    def class_name(self, obj):
        return obj.class_id.class_name  
    class_name.short_description = 'Class'

    def parent_full_name(self, obj):
        return f"{obj.parent.user.first_name} {obj.parent.user.last_name}" if obj.parent else 'N/A'
    parent_full_name.short_description = 'Parent Name'

    def teacher_name(self,obj):
        return obj.class_id.teacher_id
    teacher_name.short_description = 'Teacher Name'
         

    
admin.site.register(Student,StudentAdmin)
