from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'id')
    ordering = ['chapter']

# Register your models here.
admin.site.register(Course, CourseAdmin)
