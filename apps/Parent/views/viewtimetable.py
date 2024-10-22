from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.timetable import TimeTable
from apps.Teacher.serializer.timetable import TimeTableSerializer

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def timetable_view(request):
#     # Check if the user is authenticated
#     if request.user.is_authenticated:
#         try:
#             parent = request.user.parent
#             #print(parent_class)
#             class_id = request.GET.get("class_id")
#             if not class_id:
#                 return Response({'detail': 'class_id required'}, status=400)
#             child = parent.children.filter(class_id=class_id).first()  

#             if not child:
#                 return Response({'detail': 'No child found'}, status=404)            
#             timetable = TimeTable.objects.filter(class_id=child.class_id)

            
#             serializer = TimeTableSerializer(timetable, many=True)
#             return Response(serializer.data)

#         except AttributeError:
          
#             return Response({'detail': 'Parent information not found for the user'}, status=404)
#     return Response({'detail': 'Not authenticated'}, status=401)


@api_view(['GET'])
def timetable_view(request,class_id):
    # Check if the user is authenticated
   
    timetable = TimeTable.objects.filter(class_id=class_id)  
   
    
    serializer = TimeTableSerializer(timetable, many=True)
    
    return Response(serializer.data)

    
    
   
       
    