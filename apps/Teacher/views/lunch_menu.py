from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.lunch_menu import LunchMenu
from apps.Teacher.serializer.lunch_menu import LunchMenuSerializer


@api_view(["GET", "POST"])
def lunchmenu_view(request):
    if request.method == "GET":
        lunchmenus = LunchMenu.objects.all()
        serializer = LunchMenuSerializer(lunchmenus, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = LunchMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def lunchmenu_update(request, pk):
    try:
        lunchmenu = LunchMenu.objects.get(pk=pk)
    except LunchMenu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = LunchMenuSerializer(lunchmenu)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = LunchMenuSerializer(lunchmenu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        lunchmenu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
