from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from apps.Parent.models.writemsg import WriteMsg
from apps.Parent.serializer.writemsg import WriteMsgSerializer
from apps.Teacher.serializer.message import MessageResponseUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from apps.Teacher.models.teacher import Teacher

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def message_view(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return Response(
            {"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND
        )

    # Handle GET request: Listing messages related to the teacher's students
    if request.method == "GET":
        messages = WriteMsg.objects.filter(student__class_id__teacher_id=teacher)
        serializer = WriteMsgSerializer(messages, many=True)
        return Response(serializer.data)


    # Handle POST request: Either update a message or create a new one
    elif request.method == "POST":
        # If "id" is in request data, assume an update operation
        if "id" in request.data:
            try:
                message = WriteMsg.objects.get(
                    id=request.data["id"], 
                    student__class_id__teacher_id=teacher
                )
            except WriteMsg.DoesNotExist:
                return Response(
                    {"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND
                )

            # Update the existing message
            serializer = MessageResponseUpdateSerializer(
                message, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # For creating a new message, ensure necessary fields are present
        if "response" not in request.data:
            return Response(
                {"error": "The 'response' field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new message
        serializer = MessageResponseUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
