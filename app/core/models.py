from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email=email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


"AbstractBaseUser-func for auth system but not any fields. It can be used to create your own custom user model"
"PermissionsMixin-func for the permission feature of django and fields which are necessary for the persmission feature"
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    "Assign usermanager"
    objects = UserManager()

    "defune the field which we want to use for authentication. This is how we replace the username defult field that comes with teh default user model to our custom email field"
    USERNAME_FIELD = 'email'