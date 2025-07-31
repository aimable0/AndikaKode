from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from django.shortcuts import redirect
from django.contrib import admin

# path name here
app_name = "andikakode"

urlpatterns = [
    path("", views.loginPage, name="login"),
    path("home/", views.home, name="home"),
    path("courses/", views.courses, name="courses"),
    # path("course/<>", views.course, name="course"),
    path('course/<uuid:id>/', views.course, name='course'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.loginPage, name="logout"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path('mark-course-complete/<uuid:course_id>/', views.mark_course_complete, name='mark_course_complete'),
]

# to make sure django servers uploaded images in dev mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
