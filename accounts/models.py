from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManagement(BaseUserManager["User"]):
    def create_user(self, email: str, password: str, is_superuser=None):
        if not email:
            raise ValueError("User must have an email")
        if is_superuser is None:
            is_superuser = False

        email = self.normalize_email(email).lower()
        user = self.model(email=email, is_superuser=is_superuser)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str):
        user = self.create_user(email, password, True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    objects = UserManagement()
