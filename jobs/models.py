"""allow admins to create/update/delete jobs and users to view/apply. """
from django.db import models

class Job(models.Model):
    """Jobs/models.py ensures salary number is positive"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
