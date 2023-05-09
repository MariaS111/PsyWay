from django.dispatch import receiver
from .models import Profile, Psychologist
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


@receiver(post_save, sender=Psychologist)
def create_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, 'profile'):
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=Psychologist)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()