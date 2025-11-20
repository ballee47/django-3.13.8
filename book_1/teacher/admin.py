from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'hire_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', )
