"""allow admins to create/update/delete jobs and users to view/apply. """
from django.contrib.auth import get_user_model
from django.db import models
from users.models import CustomUser
User = get_user_model()
class Job(models.Model):
    """Jobs/models.py ensures salary number is positive"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    posted_at = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs", default=1)
    def __str__(self):
        return self.title
