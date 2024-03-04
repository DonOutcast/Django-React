from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel
from distribution.models import Distribution


class MessageLog(BaseModel):
    class States(models.TextChoices):
        __slots__ = ()
        SEND = "SEND", "Отправлено"
        DRAFT = "DRAFT", "Черновик"

    distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_logs')
    sent_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=States, default=States.DRAFT)

    def __str__(self):
        return f"Message to {self.user.username} via {self.distribution.name} [{self.status}]"
