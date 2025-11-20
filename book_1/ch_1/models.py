from django.db import models
from django.utils import timezone
# Create your models here.


  

class web_user(models.Model):
    catagory = [
    ('student','student'),
    ('teacher','teacher'),
    ('web_user','web_user'),
 
    ]
 

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='app1_images/',null=True,blank=True)
    role = models.CharField(max_length=20,choices=catagory,null=True,blank=True)
    dateandtime = models.DateTimeField(default=timezone.now)




    def __str__(self):
        return f"{self.username}:{self.role}"