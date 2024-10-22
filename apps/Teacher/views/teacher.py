from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.teacher import Teacher, Class
from apps.Teacher.serializer.teacher import TeacherSerializer, ClassSerializer
from rest_framework.permissions import AllowAny
from apps.Teacher.serializer.teacherprofile import TeacherProfileSerializer

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def teacher_list(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny])
def teacher_info(request):
    if request.user.is_authenticated:
        try:
            teacher = Teacher.objects.get(user=request.user) 
            serializer = TeacherProfileSerializer(teacher,context={'request': request})  
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(["GET"])
def class_detail(request):
    if request.user.is_authenticated:
        try:
            class_ = Class.objects.get(teacher__user=request.user)
            
            if request.method == "GET":
                serializer = ClassSerializer(class_)
                return Response(serializer.data, status=status.HTTP_200_OK)

            elif request.method == "PUT":
                serializer = ClassSerializer(class_, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif request.method == "DELETE":
                class_.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        except Class.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({'detail': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
