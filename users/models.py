"""users/models.py"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_employer = models.BooleanField(default=False)  # Distinguish employer & job seeker
    bio = models.TextField(blank=True, null=True)  # New field
    location = models.CharField(max_length=100, blank=True, null=True)  # New field
    phone = models.CharField(max_length=15, blank=True, null=True)  # New field

    def __str__(self):
        return self.username
