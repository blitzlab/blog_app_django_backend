from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_superuser(self, first_name, last_name, email, user_name, password, **other_fields):


        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Super user \"is_staff\" status must be True.")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Super user \"is_superuser\" status must be True")

        return self.create_user(first_name, last_name, email, user_name, password, **other_fields)

    def create_user(self, first_name, last_name, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_("Email address is required"))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, user_name=user_name, **other_fields)

        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email Address"), max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, unique=True)
    registered_on = models.DateTimeField(default=timezone.now)
    about = models.TextField(_("About"), null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "user_name"]


    def __str__(self):
        return self.user_name
