from django.db import models

# Create your models here.


class LoginAttempt(models.Model):
    username_or_email = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username_or_email
