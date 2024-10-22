from apps.Teacher.models.timetable import TimeTable
from apps.Teacher.serializer.timetable import TimeTableSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def timetable_view(request, class_id):
    if request.user.is_authenticated:
        timetable = TimeTable.objects.filter(class_id=class_id)
        serializer = TimeTableSerializer(timetable, many=True)
        return Response(serializer.data)
    return Response({'detail': 'Not authenticated'}, status=401)