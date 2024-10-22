from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.attendance import Attendance
from apps.Teacher.serializer.attendance import AttendanceSerializer


@api_view(['GET'])
def attendance_view(request,student_id):
    attendance = Attendance.objects.filter(student_id=student_id)
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)