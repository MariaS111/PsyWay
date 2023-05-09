from django.contrib import admin
from .models import Psychologist, Profile, CommentUserPsychologist, Session

admin.site.register(Psychologist)
admin.site.register(Profile)
admin.site.register(CommentUserPsychologist)
admin.site.register(Session)
