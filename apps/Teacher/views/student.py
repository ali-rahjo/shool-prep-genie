from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Student.models.student import Student
from apps.Teacher.models.teacher import Teacher,Class
from apps.Student.serializer.student import StudentSerializer

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def teacher_students_view(request):
   
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)

   
    if request.method == "GET":
        students = Student.objects.filter(class_id__teacher_id=teacher)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        data = request.data.copy()
        
    
        data['class_id'] = Class.objects.filter(teacher=teacher).first().id
        
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
