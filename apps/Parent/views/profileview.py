from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Parent.models.parent import Parent
from apps.Parent.serializer.parent import ParentSerializer
from apps.Student.models.student import Student
from apps.Student.serializer.student import StudentSerializer
from django.contrib.auth.models import User
from apps.Parent.serializer.parentprofile import ParentProfileSerializer


@api_view(['GET'])
def student_info(request):
    if request.user.is_authenticated:
        students = Student.objects.filter(parent__user=request.user)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)    
    return Response({'detail': 'Not authenticated'}, status=401)  

@api_view(['GET'])
def parent_info(request):
    if request.user.is_authenticated:
        try:
            parent = Parent.objects.get(user=request.user)  
            serializer = ParentProfileSerializer(parent,context={'request': request})  
            return Response(serializer.data, status=200)
        except Parent.DoesNotExist:
            return Response({"error": "Parent not found"}, status=404)
    return Response({'detail': 'Not authenticated'}, status=401)
