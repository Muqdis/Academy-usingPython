"""
URL configuration for Educatoinsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

# from django.contrib import admin
# from django.urls import path, include
# from Educatoinsystem.views import aboutus
# from Educatoinsystem.views import home_page
# from Educatoinsystem.views import courses
# from Educatoinsystem.views import course_detail
# from Educatoinsystem.views import register
# # from Educatoinsystem.views import __str__
# urlpatterns = [
#     path('admin/', admin.site.urls), 
#     # path('accounts/', include('allauth.urls')), 
#     # path('accounts/', include('accounts.urls')),
#     path('home/', home_page, name='homepage'),
#     path('aboutus/',aboutus, name='aboutus'),
#     path('courses/', courses, name='courses'),
#     path('courses/<str:course_id>/', course_detail, name='course_detail'),
#     path('signup/', register, name='register'),
#     # path('signup/',__str__, name='signup'),
#     ]
from django.contrib import admin
from django.urls import path
from Educatoinsystem.views import (
    home_page,
    aboutus,
    courses,
    course_detail,
    register,
    login_view,
    details,
    dashboard,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='homepage'),
    path('aboutus/', aboutus, name='aboutus'),
    path('courses/', courses, name='courses'),
    path('courses/<str:course_id>/', course_detail, name='course_detail'),
    path('signup/', register, name='signup'),
    path('login/', login_view, name='login'),
    path('details/', details, name='details'),
    path('dashboard/', dashboard, name='dashboard'),
]

