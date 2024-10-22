from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.Teacher.models.announcement import Announcement
from apps.Teacher.serializer.announcement import AnnouncementSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def announcement_view(request):
    
    announcements = Announcement.objects.all()
    serializer = AnnouncementSerializer(announcements, many=True)
    return Response(serializer.data)