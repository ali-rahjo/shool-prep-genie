from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.timetable import TimeTable
from apps.Teacher.serializer.timetable import TimeTableSerializer


@api_view(["GET", "POST"])
def timetable_view(request,class_id):
    
    if request.method == "GET":
        timetables = TimeTable.objects.filter(class_id=class_id)
        
        if not timetables.exists():
            return Response({"detail": "No timetable found for this class."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TimeTableSerializer(timetables, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TimeTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def timetable_update(request, pk):
    """
    Handles GET, PUT, and DELETE requests for a specific timetable identified by primary key (pk).
    """
    try:
       
        timetable = TimeTable.objects.get(pk=pk)
    except TimeTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # Serialize the timetable instance and return its data
        serializer = TimeTableSerializer(timetable)
        return Response(serializer.data)

    elif request.method == "PUT":
        # Deserialize the request data and update the existing timetable instance
        serializer = TimeTableSerializer(timetable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Delete the timetable instance
        timetable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)