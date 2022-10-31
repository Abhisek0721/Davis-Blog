from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.email
