from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)  
    description = models.TextField()

class comment(models.Model):
    posts = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date2 = models.DateTimeField(auto_now_add=True)
    content= models.TextField()