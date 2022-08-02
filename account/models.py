from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    line_id = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=20, blank=True)

# class LineOfficial(models.Model):
#     line_id = models.CharField(max_length=50)
