from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    class Meta:
        db_table = "User"

    phone = models.CharField(max_length=50)
    address = models.TextField()
