from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} ({self.age}) ({self.city})"
    
  

class gamer(models.Model):
    games = [
    ('fighting','tekken8'),
    ('aming','cod6'),
    ('stratigy','dota'),
    ('advancture','god of war')
    ]
 

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    character = models.CharField(max_length=100)
    game = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='app1_images/',null=True,blank=True)
    type = models.CharField(max_length=20,choices=games,null=True,blank=True)
    dateandtime = models.DateTimeField(default=timezone.now)




    def __str__(self):
        return f"{self.username}:{self.game}:{self.character}"