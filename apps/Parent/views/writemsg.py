# views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from apps.Parent.serializer.writemsg import WriteMsgSerializer
from apps.Parent.models.writemsg import WriteMsg
from apps.Parent.models.parent import Parent

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def write_message(request):
    if request.method == 'POST':
        serializer = WriteMsgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        try:
            parent = Parent.objects.get(user=request.user) 
        except Parent.DoesNotExist:
            return Response({"error": "Parent profile not found."}, status=status.HTTP_404_NOT_FOUND)

        messages = WriteMsg.objects.filter(parent=parent)
        serializer = WriteMsgSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
