# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Custom user model can have additional fields if needed
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)  # New field
    website = models.URLField(blank=True, null=True)  # New field
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True, null=True)  # New field

    def __str__(self):
        return self.user.username









