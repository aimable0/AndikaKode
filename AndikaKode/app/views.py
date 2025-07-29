from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "app/index.html")


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect(reverse('andikakode:login'))

    return render(request, "app/register.html", {
        "form": form
    })

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("app/index.html")
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, "app/login.html")

    return render(request, "app/login.html")

def logoutUser(request):
    # /!\: remember to add the link in the nava bar that lets the user logout
    logout(request)
    return redirect('andikakode:login')