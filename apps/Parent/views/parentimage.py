from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Parent.models.parent import Parent
from apps.Parent.serializer.parentimage import ParentImageSerializer



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_parent_image(request):
    try:
       
        parent = Parent.objects.get(user=request.user)
    except Parent.DoesNotExist:
        return Response({"error": "Parent not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ParentImageSerializer(parent, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




















