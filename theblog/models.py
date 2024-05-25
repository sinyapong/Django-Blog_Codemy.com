from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    # ชื่อเรื่อง
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    # ผู้เขียน
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # เนื้อเรื่อง
    body = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.title} | {self.author}'
    
    def get_absolute_url(self):
        # return reverse('article-detail',args=(str(self.id)))
        return reverse('home')

    
