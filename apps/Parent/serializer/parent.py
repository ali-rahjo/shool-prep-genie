from rest_framework import serializers
from apps.Parent.models.parent import Parent
from apps.Student.models.student import Student
from apps.User.serializer.user import UserSerializer
from apps.Student.serializer.student import StudentSerializer
from django.contrib.auth.models import User
from django.db import IntegrityError



class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  
    children = StudentSerializer(many=True)

    class Meta:
        model = Parent
        fields = ['id','user', 'address', 'phone_number', 'gender', 'children']

    def create(self, validated_data):
        
      

        user_data = validated_data.pop('user')
        
   
      
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            email=user_data.get('email', '')
        
        )
    
    
        
        parent = Parent.objects.create(
        user=user,
        phone_number=validated_data.get('phone_number'),
        address=validated_data.get('address'),
        gender=validated_data.get('gender')
        )
    

        children_data = validated_data.pop('children', [])
        

        for child_data in children_data:
            student_user = User.objects.create_user(
                username=child_data['username'],
                password=child_data['password'],
                first_name=child_data.get('first_name', ''),
                last_name=child_data.get('last_name', '')
            )
        

            Student.objects.create(
            user=student_user,
                parent=parent,
                age=child_data['age'],
                class_id_id=child_data['class_id'].id, 
                gender=child_data['gender'],
                username=child_data['username']
            )
        
        
    
        
        return parent
    
    