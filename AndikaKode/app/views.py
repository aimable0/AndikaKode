from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.urls import reverse
from .models import Course
from django.utils import timezone
from .models import UserCourseProgress

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
    # course = get_object_or_404(Course, id=id)
    # return render(request, "app/single_course.html", {"course": course})

    # test
    # return HttpResponse(course)
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        UserCourseProgress.objects.update_or_create(
            user=request.user,
            course=course,
            defaults={
                "is_completed": True,
                "completed_at": timezone.now()
            }
        )
        # Optionally redirect to the next course
        return redirect('andikakode:dashboard')  # or to next course

    return render(request, "app/single_course.html", {"course": course})


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
    user = request.user
    courses = Course.objects.all().order_by('chapter')  # <- Order by chapter
    progress_data = UserCourseProgress.objects.filter(user=user)

    progress_dict = {progress.course.id: progress for progress in progress_data}

    return render(request, 'app/dashboard.html', {
        'courses': courses,
        'progress_data': progress_dict
    })



    # user = request.user
    # courses = Course.objects.all()
    # progress_data = {
    #     progress.course.id: progress.is_completed
    #     for progress in UserCourseProgress.objects.filter(user=user)
    # }

    # return render(request, "app/dashboard.html", {
    #     "user": user,
    #     "courses": courses,
    #     "progress_data": progress_data,
    # })

    # return render(request, "app/dashboard.html")


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


# dealing with courses
def mark_course_complete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user

    # Mark as completed
    progress, created = UserCourseProgress.objects.get_or_create(user=user, course=course)
    progress.is_completed = True
    progress.completed_at = timezone.now()
    progress.save()

    # Get the next course (based on ID ordering)
    next_course = Course.objects.filter(id__gt=course.id).order_by('id').first()

    if next_course:
        return redirect('andikakode:course', next_course.id)
    else:
        return redirect('andikakode:dashboard')