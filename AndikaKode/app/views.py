from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.urls import reverse
from .models import Course

from django.contrib.auth import authenticate, login, logout
from uuid import UUID

# Create your views here.
def home(request):
    return render(request, "app/home.html")


def courses(request):
    courses = Course.objects.all()
    return render(request, "app/courses.html", {"courses": courses})


def course(request, id: UUID):
    # course = Course.objects.filter(title__icontains="Chapter 1").first()
    course = get_object_or_404(Course, id=id)
    return render(request, "app/single_course.html", {"course": course})

    # test
    # return HttpResponse(course)


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect(reverse("andikakode:login"))

    return render(request, "app/register.html", {"form": form})


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("andikakode:home"))
        else:
            messages.info(request, "Username or Password is incorrect")
            return render(request, "app/login.html")

    return render(request, "app/login.html")


def logoutUser(request):
    # /!\: remember to add the link in the nava bar that lets the user logout
    logout(request)
    return redirect("andikakode:login")


def dashboard(request):
    return render(request, "app/dashboard.html")


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")
