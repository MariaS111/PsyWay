from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    inf = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='users_profile_images/', blank=True, default='users_profile_images/prof_im.png')

    def __str__(self):
        return f'{self.user.username} Profile'
