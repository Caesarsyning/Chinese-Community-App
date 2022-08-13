from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    POST_CATEGORY_CHOICES=(
     ("ask", "ask"),
    ("bid", "bid"),
)
    post_category = models.CharField(default='ask',max_length=10,choices=POST_CATEGORY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='housing_author_posts') 
    likes = models.ManyToManyField(User,related_name='housing_like_posts')
    sold = models.BooleanField(default= False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.url = self.pk
        super(Post,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        # this the url to this post detail page using primarykey of this post
        return reverse('housing-post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='housing_post_comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name= 'reply')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='housing_author_comments')
    date = models.DateTimeField(auto_now_add=True)
    content= models.TextField()
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f'Comment by {self.author}'
    