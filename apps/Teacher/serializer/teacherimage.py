from rest_framework import serializers
from apps.Teacher.models.teacher import Teacher


class TeacherImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ['profile_image']
        
    def update(self, instance, validated_data):
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()
        return instance