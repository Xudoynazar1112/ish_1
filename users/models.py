from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(default="media-files/guest-user.jpg", upload_to="media-files/")
    staff = models.CharField(max_length=100, default="Kassir")
    password = models.CharField(max_length=128)
