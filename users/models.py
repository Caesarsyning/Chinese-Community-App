from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# this is like writing a script, and djangle will 
# understand it and write sql query for you


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(default='Name',max_length=50)
    year = models.CharField(default='',max_length=20)
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(default='Rotunda_logo.svg.png',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        # this the url to this post detail page using primarykey of this post
        return reverse('profile', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.url = self.user.username
        super(Profile,self).save(*args,**kwargs)
