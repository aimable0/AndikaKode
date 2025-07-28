from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aimable", views.aimable, name="aimable"),
    # let's create some parametirized paths
    path("<str:name>", views.greet, name="greet"),
]
