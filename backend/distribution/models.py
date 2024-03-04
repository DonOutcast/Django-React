from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel


class Distribution(BaseModel):
    name = models.CharField(max_length=100)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name='distributions')

    def __str__(self):
        return self.name
