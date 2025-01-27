from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    national_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.username