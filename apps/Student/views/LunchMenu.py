from apps.Teacher.models.lunch_menu import LunchMenu
from apps.Teacher.serializer.lunch_menu import LunchMenuSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lunchmenu_view(request):
    if request.user.is_authenticated:
        lunchmenu = LunchMenu.objects.all()
        # Serializer the fetched menu data
        serializer = LunchMenuSerializer(lunchmenu, many=True)
        return Response(serializer.data)
    return Response({'detail': 'Not authenticated'}, status=401)