from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.teacher import Teacher
from apps.Teacher.serializer.teacherimage import TeacherImageSerializer



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_teacher_image(request):
    try:
       
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TeacherImageSerializer(teacher, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




















