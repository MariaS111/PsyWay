from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Psychologist


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Psychologist.objects.get(email=email)
            if user.check_password(password):
                return user
        except Psychologist.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Psychologist.objects.get(pk=user_id)
        except Psychologist.DoesNotExist:
            return None