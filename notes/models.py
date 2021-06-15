from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    subject = models.CharField(max_length=30, blank=False)
    text = models.CharField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='note',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
