from django.db import models

# Create your models here.
class Task(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    completed=models.CharField(max_length=20)
