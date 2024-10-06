from django.db import models

# Create your models here.

class ApiPath(models.Model):
    task_list=models.CharField(max_length=100)
    task_detail=models.CharField(max_length=100)
    task_create=models.CharField(max_length=100)
    task_update=models.CharField(max_length=100)
    task_select_update=models.CharField(max_length=100)
    task_delete=models.CharField(max_length=100)
