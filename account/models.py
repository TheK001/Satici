from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password,  **extra_field):
        if not email:
            raise ValueError("emaili mutleq daxil edin!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email, password, **extra_field):
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)
        extra_field.setdefault("is_active", True)

        if extra_field.get("is_staff") is not True:
            raise ValueError("is_staff must be True")

        if extra_field.get("is_superuser") is not True:
            raise ValueError("is_superuser must be True")
        
        return self.create_user(email, password, **extra_field)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []    
    objects = UserManager()
