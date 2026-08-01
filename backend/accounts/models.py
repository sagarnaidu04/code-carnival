from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model for Code Carnival.
    We start with Django's User and extend it later.
    """
    pass