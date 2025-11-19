from django.contrib import admin
from .models import Course



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'start_date', 'end_date', 'max_students')
    search_fields = ('name', 'code')
    list_filter = ('start_date', 'end_date')
    ordering = ('code',)
