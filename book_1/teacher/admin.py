from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    # Columns shown in list view
    list_display = (
        'first_name', 'last_name', 'email', 'phone',
        'role', 'is_active', 'hire_date','contract_end_date',
    )

    # Clickable columns
    list_display_links = (
        'first_name', 'last_name', 'email', 'phone',
        'role', 'is_active', 'hire_date','contract_end_date',
    )

    # Search bar fields
    search_fields = ('first_name', 'last_name', 'email', 'phone')

    # Filters on the right side
    list_filter = ('role', 'is_active')

    # Default ordering
    ordering = ('last_name', 'first_name')

    # Form layout
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Employment Details', {
            'fields': ('role', 'is_active', 'hire_date','contract_end_date', 'courses')
        }),
    )

    # Read-only fields (optional)
    readonly_fields = ('hire_date',)
