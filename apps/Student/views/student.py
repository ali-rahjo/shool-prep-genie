from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from apps.Student.models.student import Student
from apps.Student.serializer.student import StudentSerializer
from apps.Teacher.models.teacher import Class
from rest_framework.permissions import AllowAny

@api_view(['Get', 'Post'])
@permission_classes([AllowAny])
def student_list(request):
        if request.method == "GET":
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == "POST":
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny]) 
def student_detail(request,pk):
    student = Student.objects.filter(pk=pk)

    if student is None:
        return Response({"error": "Student not found"})
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        
    elif request.method == "DELETE":
        student


    