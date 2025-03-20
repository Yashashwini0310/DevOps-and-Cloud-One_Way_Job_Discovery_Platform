"""users/models.py"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # phone = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number field
    is_employer = models.BooleanField(default=False)  # Flag to differentiate employer & job seeker

    def __str__(self):
        return self.username

