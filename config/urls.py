"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "SCHOOLPREP GENIE"
admin.site.index_title = "A School mate........."   #  Replace with  suitable sentence :()
admin.site.site_title = "WELCOME TO SCHOOL PREP GENIE"



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/auth/', include('dj_rest_auth.urls')),

    path('api/v1/user/', include('apps.User.urls',namespace='user-urls')),
    path('api/v1/parent/', include('apps.Parent.urls',namespace='parent-urls')),
    path('api/v1/student/', include('apps.Student.urls',namespace='student-urls')),
    path('api/v1/teacher/', include('apps.Teacher.urls',namespace='teacher-urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
