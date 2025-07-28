from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django import forms



# we need a form
class NewTaskForm(forms.Form):
    task_name = forms.CharField(label="task")

# Create your views here.
def index(request):

    # how do we deal with sessions (attempt 1).
    if "tasks" not in request.session:
        request.session['tasks'] = []

    return render(request, "todo/index.html", {
        "tasks": request.session['tasks'],
    })

# add tasks.
def add(request):
    if (request.method == "POST"):
        task = request.POST.get("task_name")
        request.session['tasks'] += [task]
        return redirect(reverse("todo:index"))

    return  render(request, "todo/add.html", {"form": NewTaskForm})



