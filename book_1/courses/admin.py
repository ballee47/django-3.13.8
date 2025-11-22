from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    # Columns shown in list view
    list_display = ('name', 'code', 'start_date', 'end_date', 'max_students', 'duration')

    # Clickable columns
    list_display_links = ('name', 'code', 'start_date', 'end_date', 'max_students', 'duration')


    # Search bar fields
    search_fields = ('name', 'code')

    # Filters on the right side
    list_filter = ('start_date', 'end_date')

    # Default ordering
    ordering = ('code',)

    # Layout of form edit page
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'code', 'description')
        }),
        ('Schedule', {
            'fields': ('start_date', 'end_date')
        }),
        ('Capacity', {
            'fields': ('max_students',)
        }),
    )

    # Custom method for list_display
    def duration(self, obj):
        """Show total days between start and end date."""
        return (obj.end_date - obj.start_date).days
    duration.short_description = "Duration (days)"
