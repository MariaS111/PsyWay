from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Psychologist(AbstractBaseUser):
    # username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    bio = models.TextField()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField('Psychologist', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='psychologists_profile_images/', blank=True,
                                      default='psychologists_profile_images/prof_im.png')
    is_psychologist = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'


class CommentUserPsychologist(models.Model):
    psychologist = models.ForeignKey('psychologists.Psychologist', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.psychologist.first_name} {self.psychologist.last_name}"


class Session(models.Model):
    STATUS_CHOICES = [
        ('await', 'Await'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    psychologist = models.ForeignKey('psychologists.Psychologist', on_delete=models.CASCADE)
    users = models.ManyToManyField('users.User', related_name='session_users')
    date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)

    def __str__(self):
        usernames = ', '.join([user.username for user in self.users.all()])
        return f"Session {usernames} with {self.psychologist.first_name} {self.psychologist.last_name}"