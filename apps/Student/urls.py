from django.urls import path
from . import views

app_name = 'Student'
urlpatterns = [
    path('list/', views.student_list, name='student_list'),
    path('view/lunchmenu/', views.lunchmenu_view, name='view-lunchmenu'),
    path('view/timetable/<int:class_id>/', views.timetable_view, name='view-timetable'),
    path('view/announcement/', views.announcement_view, name='view-announcement'),
    path('profile/', views.student_profile, name='view-profile')
]
