from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    types = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    info = models.TextField(null=True, blank=True)
    advantage = models.TextField(null=True, blank=True)
    disadvantage = models.TextField(null=True, blank=True)
    image = models.ImageField(default = 'Rotunda_logo.svg.png',null=True, blank=True,upload_to='profile_pics')
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='housing101_author_posts') 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.url = self.pk
        super(Post,self).save(*args,**kwargs)

class offPost(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    types = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    info = models.TextField(null=True, blank=True)
    advantage = models.TextField(null=True, blank=True)
    disadvantage = models.TextField(null=True, blank=True)
    image = models.ImageField(default = 'Rotunda_logo.svg.png',null=True, blank=True,upload_to='profile_pics')
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='housing101_author_offposts') 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.url = self.pk
        super(offPost,self).save(*args,**kwargs)
