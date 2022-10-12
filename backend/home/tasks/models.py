from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Task(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120, blank=True, default='')
    description = models.CharField(max_length=120, blank=True, default='No description')
    done = models.BooleanField(default=False, blank=True)