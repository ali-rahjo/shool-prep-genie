
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Parent.models.parent import Parent
from apps.Parent.serializer.parent import ParentSerializer
from apps.Student.models.student import Student
from apps.Student.serializer.student import StudentSerializer
from django.contrib.auth.models import User
from apps.Teacher.models.teacher import Class
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from apps.Parent.utils import send_verification_email
from django.db import transaction
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPRecipientsRefused





@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  
def parent_list(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        parent_data = request.data.get('user')
        children_data = request.data.get('children')
        gender = request.data.get('gender')
        address = request.data.get('address')
        phone_number = request.data.get('phone_number')
        
        
       
        try:
           
            with transaction.atomic():
               
                if Parent.objects.filter(phone_number=phone_number).exists():
                    return Response(
                        {"error": f"Phone number '{phone_number}' already exists. Please provide a different phone number."},
                        status=status.HTTP_400_BAD_REQUEST
                    )

               
                if User.objects.filter(username=parent_data['username']).exists():
                    return Response(
                        {"error": f"Username '{parent_data['username']}' already exists. Please choose a different username."},
                        status=status.HTTP_400_BAD_REQUEST
                    )

               
                parent_user = User.objects.create_user(
                    username=parent_data['username'],
                    password=parent_data['password'],
                    first_name=parent_data.get('first_name', ''),
                    last_name=parent_data.get('last_name', ''),
                    email=parent_data['email'],
                    is_active=False  
                )
                print("Created Parent User:", parent_user.username)

               
                parent = Parent.objects.create(
                    user=parent_user,  
                    address=address,
                    phone_number=phone_number,
                    gender=gender
                )
                print("Created Parent:", parent.user.get_full_name())

                
                
                try:
                    
                    send_verification_email(parent_user, request)
                    
                except SMTPRecipientsRefused:
                  
                    return Response(
                        {"error": f"The recipient email address '{parent_user.email}' is invalid. Please provide a valid email address."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                except BadHeaderError:
                    
                    return Response({"error": "Invalid header found."}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
                students = []
                for child_data in children_data:
                    
                    if Student.objects.filter(username=child_data['username']).exists():
                        raise IntegrityError(f"Student username '{child_data['username']}' already exists. Please choose a different username.")

                    student_user, created = User.objects.get_or_create(
                        username=child_data['username'],
                        defaults={
                            'first_name': child_data.get('first_name', ''),
                            'last_name': child_data.get('last_name', '')
                        }
                    )

                    if created:
                        student_user.set_password(child_data['password'])
                        student_user.save()
                        print("Created Student User:", student_user.username)
                    else:
                        raise IntegrityError(f"User '{student_user.username}' already exists.")

                   
                    try:
                        class_instance = Class.objects.get(id=child_data['class_id'])
                    except Class.DoesNotExist:
                        raise IntegrityError("Class not found")

                    
                    student = Student.objects.create(
                        user=student_user,
                        parent=parent,
                        age=child_data['age'],
                        class_id=class_instance,
                        gender=child_data['gender'],
                        username=student_user.username,
                        first_name=child_data.get('first_name', ''),
                        last_name=child_data.get('last_name', ''),
                        #teacher_name=child_data['teacher_name']
                    )

                   
                    class_info = {
                        "id": student.class_id.id,
                        "class_name": student.class_id.class_name,
                        "academic_year_start": student.class_id.academic_year_start,
                        "academic_year_end": student.class_id.academic_year_end,
                        "grade": student.class_id.grade,
                       # "teacher_name": student.teacher_name
                    }

                    students.append({
                        "first_name": student.user.first_name,
                        "last_name": student.user.last_name,
                        "age": student.age,
                        "class_id": class_info,
                        "gender": student.gender,
                        "username": student.user.username,
                        #"teacher_name": student.teacher_name
                    })

               
                response_data = {
                    "user": {
                        "username": parent_user.username,
                        "first_name": parent_user.first_name,
                        "last_name": parent_user.last_name,
                        "email": parent_user.email,
                    },
                    "address": address,
                    "phone_number": phone_number,
                    "gender": gender,
                    "children": students
                }

                return Response(response_data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
           
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )


  
    
