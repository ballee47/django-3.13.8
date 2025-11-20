from django.db import models 
from courses.models import Course  # link to courses

class Teacher(models.Model):
    ROLE_CHOICES = (
        ('assistant', 'Assistant Teacher'),
        ('senior', 'Senior Teacher'),
        ('head', 'Head Teacher'),
        ('temporary', 'Temporary'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='assistant')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
