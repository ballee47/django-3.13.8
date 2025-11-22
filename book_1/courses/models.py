from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=100)             # Name of the course
    code = models.CharField(max_length=10, unique=True) # Unique code like MATH101
    description = models.TextField(blank=True)          # Optional course description

    # Use localdate to avoid timezone datetime issues
    start_date = models.DateField(default=timezone.localdate, null=True, blank=True)
    end_date = models.DateField(default=timezone.localdate, null=True, blank=True)

    max_students = models.PositiveIntegerField(default=30)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        ordering = ['code']
        verbose_name = "Course"
        verbose_name_plural = "Courses"
