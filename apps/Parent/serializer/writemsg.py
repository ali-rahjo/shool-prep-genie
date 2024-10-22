# serializers.py

from rest_framework import serializers
from apps.Parent.models.writemsg import WriteMsg
from apps.Parent.models.parent import Parent
from apps.Student.models.student import Student
from apps.Teacher.models.teacher import Teacher
from datetime import datetime

class WriteMsgSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    parent_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    
    class Meta:
        model = WriteMsg  
        fields = ['id', 'parent', 'parent_name', 'student', 'student_name', 'teacher_name', 'class_name','text_msg','response','date']
        
    def get_parent_name(self, obj):
        return f"{obj.parent.user.first_name} {obj.parent.user.last_name}"
    
    def get_teacher_name(self, obj):
        return obj.student.class_id.teacher_id.user.get_full_name()

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"
    
    def get_class_name(self,obj):
        return obj.student.class_id.class_name
    
    def get_date(self, obj):
        return obj.date.date() if isinstance(obj.date, datetime) else obj.date    

        

    def validate_text_msg(self, value):
        if not value:
            raise serializers.ValidationError("Message text cannot be empty.")
        return value
    
    def validate(self, data):
        parent = data.get('parent')
        student = data.get('student')
        text_msg = data.get('text_msg')

      
        if WriteMsg.objects.filter(parent=parent, student=student, text_msg=text_msg).exists():
            raise serializers.ValidationError("Message already exists.")

        return data

    def create(self, validated_data):
        return WriteMsg.objects.create(**validated_data)
   