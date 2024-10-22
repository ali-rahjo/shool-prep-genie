from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Parent.models.parent import Parent
from apps.Parent.serializer.parent import ParentSerializer
from apps.Student.models.student import Student
from apps.Student.serializer.student import StudentSerializer
from django.contrib.auth.models import User


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    try:
        parent_instance = Parent.objects.get(user=request.user)
    except Parent.DoesNotExist:
        return Response({"error": "Parent profile not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ParentSerializer(parent_instance, data=request.data, partial=True)
    
    if serializer.is_valid():
        user_data = request.data.get('user', {})
        if user_data:
            user_instance = parent_instance.user
            user_instance.first_name = user_data.get('first_name', user_instance.first_name)
            user_instance.last_name = user_data.get('last_name', user_instance.last_name)
            user_instance.email = user_data.get('email', user_instance.email)
            user_instance.save()
        
    
        parent_instance.phone_number = request.data.get('phone_number', parent_instance.phone_number)
        parent_instance.address = request.data.get('address', parent_instance.address)
        parent_instance.gender = request.data.get('gender', parent_instance.gender)
        parent_instance.save()
        parent_data = {
            "id": parent_instance.id,
            "user": {
                "first_name": parent_instance.user.first_name,
                "last_name": parent_instance.user.last_name,
                "email": parent_instance.user.email
            },
            "phone_number": parent_instance.phone_number,
            "address": parent_instance.address,
            "gender": parent_instance.gender
        }


        # children_data = request.data.get('children', [])
        # for child_data in children_data:
        #     child_instance = Student.objects.filter(parent=parent_instance, id=child_data.get('id')).first()

        #     if child_instance:
        #         child_instance.user.first_name = child_data.get('first_name', child_instance.user.first_name)
        #         child_instance.user.last_name = child_data.get('last_name', child_instance.user.last_name)
        #         child_instance.age = child_data.get('age', child_instance.age)
        #         child_instance.gender = child_data.get('gender', child_instance.gender)
        #         child_instance.class_id_id = child_data.get('class_id', child_instance.class_id_id)
        #         child_instance.user.save()
        #         child_instance.save()
        #     else:
              
        #         student_user = User.objects.create_user(
        #             username=child_data['username'],
        #             password=child_data['password'],
        #             first_name=child_data.get('first_name', ''),
        #             last_name=child_data.get('last_name', '')
        #         )

        #         Student.objects.create(
        #             user=student_user,
        #             parent=parent_instance,
        #             age=child_data['age'],
        #             class_id_id=child_data['class_id'],
        #             gender=child_data['gender']
        #         )

        return Response(parent_data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
