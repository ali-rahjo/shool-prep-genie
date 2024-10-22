from rest_framework import serializers
from apps.Parent.models.leave import Leave
from apps.Parent.models.parent import Parent
from apps.Student.models.student import Student
from datetime import datetime

class LeaveSerializer(serializers.ModelSerializer):
    
    parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    parent_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
 

    class Meta:
        model = Leave
        fields = ['id','parent','parent_name','student','student_name','class_name','date','leave_type', 'status', 'leave_description', 'start_date', 'end_date','teacher_name']
        read_only_fields = ['status'] 
        
    def get_parent_name(self, obj):
        return obj.parent.user.first_name + " " + obj.parent.user.last_name
    
        
    def get_class_name(self, obj):
        return obj.student.class_id.class_name
    
    def get_teacher_name(self, obj):
      
        return obj.student.class_id.teacher_id.user.get_full_name()

    def get_date(self, obj):
        return obj.date.date() if isinstance(obj.date, datetime) else obj.date    

    def get_student_name(self, obj):
        return obj.student.first_name + " " + obj.student.last_name  
    
    def to_representation(self, instance):
        
        representation = super().to_representation(instance)
        
        
        if isinstance(representation['date'], datetime):
            representation['date'] = representation['date'].date()
        if isinstance(representation['start_date'], datetime):
            representation['start_date'] = representation['start_date'].date()
        if isinstance(representation['end_date'], datetime):
            representation['end_date'] = representation['end_date'].date()
        
        return representation
    
    
    def validate(self, data):
        
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        if isinstance(start_date, datetime):
            data['start_date'] = start_date.date()
        if isinstance(end_date, datetime):
            data['end_date'] = end_date.date()

        if start_date and end_date:
            
            if start_date > end_date:
                raise serializers.ValidationError("Start date cannot be later than end date.")
        else:
            raise serializers.ValidationError("Both start date and end date must be provided.")

        return data 

    def create(self, validated_data):
        
        leave_instance = Leave.objects.create(**validated_data)
        return leave_instance