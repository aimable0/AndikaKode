from . import views
from django.urls import path

# path name here
app_name = 'andikakode'

urlpatterns = [
    path("", views.index, name='index'),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
]