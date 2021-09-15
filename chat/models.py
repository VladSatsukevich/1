from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField( default=False )
    closed = models.BooleanField( default=False )
    freeze = models.BooleanField( default=False )

    def __str__(self):
        return self.message

    class Meta:
        verbose_name: "Вопрос"
        verbose_name_plural: "Вопросы"


