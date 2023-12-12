from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(null = True)
    dob = models.DateField(null=True)
    profile_image = models.ImageField(null=True)
