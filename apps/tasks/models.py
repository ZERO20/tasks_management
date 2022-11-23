from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """Model definition for Task."""
    COMPLETE = 'complete'
    INCOMPLETE = 'incomplete'
    STATUS_CHOICES = [
        (COMPLETE, 'Complete'),
        (INCOMPLETE, 'Incomplete'),
    ]
    name = models.CharField(verbose_name="Name", max_length=200)
    description = models.TextField(verbose_name="Description")
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default=INCOMPLETE)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name
