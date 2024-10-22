from django.urls import path
from . import views

app_name = "Teacher"
urlpatterns = [
    path("registration/", views.teacher_list, name="teacher-list"),
    path("view/profile/", views.teacher_info, name="teacher-profile-view"),
    path('profile/image/', views.update_teacher_image, name='teacher_profile_image'),
    path("classes/", views.class_detail, name="class-detail"),
    path("timetable/view/<int:class_id>/", views.timetable_view, name="view-timetable"),
    path("timetable/create/<int:class_id>/", views.timetable_view, name="create-timetable"),
    path("timetable/update/<int:pk>/", views.timetable_update, name="timetable-update"),
    path("lunchmenu/view/", views.lunchmenu_view, name="view-lunchmenu"),
    path("lunchmenu/create/", views.lunchmenu_view, name="create-lunchmenu"),
    path("lunchmenu/update/<int:pk>/", views.lunchmenu_update, name="update-lunchmenu"),
    path("leave/view/request/", views.leave_request_view, name="leave-request-view"),
    path("leave/update/<int:pk>/", views.update_leave_status, name="update-leave-status"),
    path("message/view/", views.message_view, name="message-view"),
    path("message/write/", views.message_view, name="update-message-response"),
    path("attendance/view/", views.attendance_view, name="attendance-view"),
    path("attendance/mark/<int:pk>/", views.mark_attendance, name="mark-attendance"),
    path("announcement/view/", views.announcement_view, name="announcement-view"),
    path("announcement/create/", views.announcement_create, name="announcement-create"),
    path("students/", views.teacher_students_view, name='teacher-students'),
]


"""
app_name = "Teacher"
urlpatterns = [
    path("registration/", views.teacher_list, name="teacher-list"),
    path("<int:pk>/", views.teacher_detail, name="teacher-detail"),
    path("classes/<int:pk>/", views.class_detail, name="class-detail"),

    # Timetable URLs
    path("timetable/view/", timetable_view, name="timetable-detail"),
    path("timetable/update/<int:pk>/", timetable_update, name="timetable-update"),

    # Lunch Menu URLs
    path("lunchmenu/view/", lunchmenu_list, name="lunchmenu-list"),
    path("lunchmenu/update/<int:pk>/", lunchmenu_update, name="lunchmenu-detail"),
]"""
