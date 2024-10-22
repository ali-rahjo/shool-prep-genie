from rest_framework import serializers
from apps.Parent.models.parent import Parent
from apps.User.serializer.user import UserSerializer
from apps.Teacher.models.teacher import Class

class TeacherProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()  
    class_id = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    academic_year_start = serializers.SerializerMethodField()
    academic_year_end = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    profile_image = serializers.ImageField(required=False)
    profile_image_url = serializers.SerializerMethodField()


    class Meta:
        model = Parent
        fields = ['id', 'user', 'gender', 'class_id', 'class_name', 'academic_year_start', 'academic_year_end', 'grade', 'profile_image', 'profile_image_url']  
     
     
    def get_class_id(self, obj):
        teacher_class = Class.objects.filter(teacher_id=obj).first()
        return teacher_class.id if teacher_class else None

    def get_class_name(self, obj):
        teacher_class = Class.objects.filter(teacher_id=obj).first()
        return teacher_class.class_name if teacher_class else None
    
    def get_academic_year_start(self, obj):
        teacher_class = Class.objects.filter(teacher_id=obj).first()
        return teacher_class.academic_year_start if teacher_class else None

    def get_academic_year_end(self, obj):
        teacher_class = Class.objects.filter(teacher_id=obj).first()
        return teacher_class.academic_year_end if teacher_class else None

    def get_grade(self, obj):
        teacher_class = Class.objects.filter(teacher_id=obj).first()
        return teacher_class.grade if teacher_class else None
     
 
        
    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)  
        return None    