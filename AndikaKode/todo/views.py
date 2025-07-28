from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django import forms



# we need a form
class NewTaskForm(forms.Form):
    task_name = forms.CharField(label="task")
    # priority = forms.IntegerField(label="priority")

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
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # This will help validate whether:
            # 1. the data provided by the user is meeting the required conditions and specifications
            # 2. This are specified while creating input for the form (when creating the form class)
            task = form.cleaned_data['task_name']
            request.session['tasks'] += [task]
            return redirect(reverse("todo:index"))
        else:
            # Let's send back the form so that we can also display the error that made the form invalid
            return render(request,"todo/add.html", {"form": form})

    return  render(request, "todo/add.html", {"form": NewTaskForm()})



