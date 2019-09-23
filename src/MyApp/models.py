from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length = 200)
    added_date = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length = 30, blank=True,null=True)
