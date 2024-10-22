
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Student.models import Student
from apps.Student.serializer.student import StudentSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def student_profile(request):
    try:
        student = Student.objects.get(username=request.user.username)  
    except Student.DoesNotExist:
        return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)
