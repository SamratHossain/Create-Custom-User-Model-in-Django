from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
from account.usermanager import AccountUserManager

class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    dateofbirth = models.DateField()

    joinat = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name', 'phone', 'gender', 'dateofbirth']

    def __str__(self):
        return self.email