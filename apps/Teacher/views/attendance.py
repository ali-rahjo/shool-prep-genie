

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from apps.Student.models import Student
from apps.Teacher.models import Attendance
from apps.Teacher.serializer.attendance import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated
from apps.Teacher.models.teacher import Teacher ,Class

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def attendance_view(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return Response(
            {"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND
        )

    today = timezone.now().date()

    # Fetch the class where the teacher is assigned
    try:
        assigned_class = Class.objects.get(teacher_id=teacher.id)
    except Class.DoesNotExist:
        return Response(
            {"error": "Class not found for this teacher."},
            status=status.HTTP_404_NOT_FOUND,
        )

    # Fetch attendance records for all students in the teacher's class
    attendance_records = Attendance.objects.select_related('student__user', 'student__class_id').filter(
        student__class_id=assigned_class.id, date=today
    )

    if not attendance_records.exists():
        return Response(
            {"message": "No attendance records found for today."},
            status=status.HTTP_200_OK,
        )

    serializer = AttendanceSerializer(attendance_records, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def mark_attendance(request, pk):

    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return Response(
            {"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND
        )

    # Fetch the class where the teacher is assigned
    try:
        assigned_class = Class.objects.get(teacher_id=teacher.id)
    except Class.DoesNotExist:
        return Response(
            {"error": "Class not found for this teacher."},
            status=status.HTTP_404_NOT_FOUND,
        )

    # Fetch the student in the class
    try:
        student = Student.objects.get(id=pk, class_id=assigned_class.id)
    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found or not in the teacher's class."},
            status=status.HTTP_404_NOT_FOUND,
        )

    today = timezone.now().date()

    attendance, created = Attendance.objects.get_or_create(
        student=student,
        date=today,
        defaults={
            "is_present": request.data.get("is_present", True),
            "teacher": teacher,
        },
    )

    if not created:
        attendance.is_present = request.data.get("is_present", attendance.is_present)
        attendance.teacher = teacher
        attendance.save()

    serializer = AttendanceSerializer(attendance)
    return Response(serializer.data, status=status.HTTP_200_OK)
