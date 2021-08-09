from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    about = models.CharField(max_length=500, verbose_name='About')
    phone = models.CharField(max_length=25, verbose_name='Phone')
    address = models.CharField(max_length=100, verbose_name='Address')
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Author')
    text = models.TextField(max_length='1200', verbose_name='Post text')
    post_dt = models.DateField(auto_now=True, verbose_name='Post created time')

    def __str__(self):
        return f"{self.author}'s post created at {self.post_dt}"

