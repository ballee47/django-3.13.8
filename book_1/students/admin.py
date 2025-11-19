
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'roll_number', 'email', 'enrollment_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'roll_number', 'email')
    list_filter = ('is_active', 'courses')
