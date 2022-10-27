import email
from enum import unique
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Account(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.JSONField() # JSONField because it will be stored in encripted form
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.username
