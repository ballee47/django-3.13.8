
from django.db import models
from courses.models import Course  # link to courses
from teacher.models import Teacher  # link to teachers



class Student(models.Model):

    ROLE_CHOICES = (
        ('regular', 'Regular Student'),
        ('monitor', 'Class Monitor'),
        ('prefect', 'Prefect'),
        ('probation', 'On Probation'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular')
    course = models.ForeignKey('courses.Course', blank=True, null=True ,on_delete=models.CASCADE,related_name='students')
    teacher = models.ForeignKey('teacher.Teacher', blank=True, null=True ,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"
