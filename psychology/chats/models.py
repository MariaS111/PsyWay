from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_private = models.BooleanField(default=True)
    psychologists = models.ManyToManyField('psychologists.Psychologist', related_name='chats_ps', blank=True)
    users = models.ManyToManyField('users.User', related_name='chats_users', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} at {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}: {self.content}'