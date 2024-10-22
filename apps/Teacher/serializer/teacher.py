from rest_framework import serializers
from apps.Teacher.models.teacher import Teacher, Class
from apps.User.serializer import UserSerializer

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'academic_year_start', 'academic_year_end', 'grade','teacher_id']


class TeacherSerializer(serializers.ModelSerializer):
    
    user = UserSerializer() 
    class_id = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    academic_year_start = serializers.SerializerMethodField()
    academic_year_end = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
   

    
    class Meta:
        model = Teacher
        fields = ["id", "user", "gender","class_id", "class_name","academic_year_start", "academic_year_end", "grade"]
        
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
     

    def create(self, validated_data):
        user_data = validated_data.pop('user')  
       
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()  
       
       
        teacher = Teacher.objects.create(user=user, **validated_data)

        return teacher



        


