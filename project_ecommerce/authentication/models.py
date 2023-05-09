from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class NewUserModel(AbstractUser):
    # username = models.CharField()
    def __str__(self):
        return self.username

