from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High","High")
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    is_completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.title

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tasks/images')

    def __str__(self):
        return self.task.title