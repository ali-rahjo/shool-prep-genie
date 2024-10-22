from rest_framework import serializers
from rest_framework.exceptions import ValidationError 
from apps.Teacher.models.timetable import TimeTable

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta : 
        model= TimeTable
        fields = '__all__'

    def validate(self, data):
        teacher = data.get('teacher')
        class_id = data.get('class_id')
        
        if TimeTable.objects.filter(teacher=teacher, class_id=class_id).exists():
            raise ValidationError("This teacher already has a timetable for this class.")
        
        return data
 
