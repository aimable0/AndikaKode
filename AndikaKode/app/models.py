from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    course_card = models.ImageField(upload_to="img/course_cards/")
    description = models.TextField()
    video_link = models.URLField()
    goals = models.JSONField(default=list, blank=True)
    topics = models.JSONField(default=list, blank=True)
    exercises = models.JSONField(default=list, blank=True)
    activities = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title

    def display_overview(self):
        return f"{self.title}\n\n{self.description}\nGoals: {', '.join(self.goals)}"

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        self.save()

    def add_goal(self, goal):
        self.goals.append(goal)
        self.save()

    def get_video(self):
        return f"Watch the course video here: {self.video_link}"


# from .models import Course
class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "course")
