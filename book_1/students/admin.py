from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # Columns shown in the list page
    list_display = (
        'first_name', 'last_name', 'roll_number', 'email',
        'course', 'role', 'is_active', 'enrollment_date','teacher'
    )

    # Make these fields clickable
    list_display_links = (
        'first_name', 'last_name', 'roll_number', 'email',
        'course', 'role', 'is_active', 'enrollment_date'
    )

    # Search bar fields
    search_fields = ('first_name', 'last_name', 'roll_number', 'email')

    # Filters on the right side
    list_filter = ('role', 'is_active', 'course')

    # Default ordering
    ordering = ('last_name', 'first_name')

    # Form layout
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'roll_number')
        }),
        ('Contact Details', {
            'fields': ('email', 'phone')
        }),
        ('Academic Info', {
            'fields': ('course', 'role', 'teacher')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

    # Read-only fields (optional)
    readonly_fields = ('enrollment_date',)
