from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.Parent.models.leave import Leave
from apps.Parent.serializer.leave import LeaveSerializer
from apps.Student.models.student import Student
from apps.Parent.models.parent import Parent
from django.db.models import Q
from datetime import datetime

@api_view(['GET', 'POST'])
def parent_leave_list_create(request):
    
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=401)

    if request.method == 'GET':
        try:
            parent = Parent.objects.get(user=request.user)
        except Parent.DoesNotExist:
            return Response({"detail": "User has no associated parent record."}, status=404)

        leaves = Leave.objects.filter(student_id__parent=parent)
        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        parent_id = request.data.get('parent_id')
        student_id = request.data.get('student_id')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        
        if isinstance(start_date, datetime):
            request.data['start_date'] = start_date.date()
        if isinstance(end_date, datetime):
            request.data['end_date'] = end_date.date()

        try:
            parent = Parent.objects.get(id=parent_id)
        except Parent.DoesNotExist:
            return Response({'error': 'Invalid parent_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=status.HTTP_400_BAD_REQUEST)

        
        overlapping_leaves = Leave.objects.filter(
            Q(start_date__lte=end_date, end_date__gte=start_date) | Q(status='pending'),
            student=student  
        )

        if overlapping_leaves.exists():
            return Response({'error': 'Leave already requested or pending for the same period.'}, status=status.HTTP_400_BAD_REQUEST)

       
        validated_data = {
            'leave_type': request.data.get('leave_type'),
            'leave_description': request.data.get('leave_description'),
            'start_date': start_date,
            'end_date': end_date,
            'parent': parent_id,
            'student': student_id
        }

        serializer = LeaveSerializer(data=validated_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
