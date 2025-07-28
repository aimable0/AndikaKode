from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello you got me!")
    name = "Aimable"
    return render(request, "app/index.html", {"name": name})

def aimable(request):
    return HttpResponse("Hello Aimabii")

def greet(request, name):
    return HttpResponse(f"Hello, Mr/Madam {name}")