from . import views
from django.urls import path

# path name here
app_name = 'andikakode'

urlpatterns = [
    path("", views.home, name='home'),
    path("courses/", views.courses, name='courses'),
    path("course/", views.course, name='course'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]