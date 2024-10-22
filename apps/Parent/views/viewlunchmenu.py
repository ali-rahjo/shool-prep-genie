from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.Teacher.models.lunch_menu import LunchMenu
from apps.Teacher.serializer.lunch_menu import LunchMenuSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lunchmenu_view(request):
    if request.user.is_authenticated:
        try:
            
            lunchmenu = LunchMenu.objects.all()
            serializer = LunchMenuSerializer(lunchmenu, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response({'detail': str(e)}, status=500)
    
    return Response({'detail': 'Not authenticated'}, status=401)
