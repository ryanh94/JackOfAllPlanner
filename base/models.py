from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

class Task(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Priority(models.TextChoices):
        UNKNOWN = "UNKNOWN"
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.UNKNOWN,
    )