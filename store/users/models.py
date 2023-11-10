from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    users_images = models.ImageField(
        upload_to='users_image/',
        blank=True,
        null=True
    )
