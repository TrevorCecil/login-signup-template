from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(null=True, blank=True,default='img.png')

    def __str__(self):
        return str(self.user)
