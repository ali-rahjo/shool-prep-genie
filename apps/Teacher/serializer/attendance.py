from rest_framework import serializers
from apps.Teacher.models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    
    student_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    student_id = serializers.SerializerMethodField()
    
    class Meta:
        model = Attendance
        fields = ['id','student_id','student_name', 'teacher_name', 'class_name', 'date', 'is_present']
        
        
    
    def get_student_id(self, obj):
        return obj.student.id     

    def get_student_name(self, obj):
        return f"{obj.student.user.first_name} {obj.student.user.last_name}"

    def get_teacher_name(self, obj):
        return f"{obj.teacher.user.first_name} {obj.teacher.user.last_name}"

    def get_class_name(self, obj):
        
        return obj.student.class_id.class_name

  