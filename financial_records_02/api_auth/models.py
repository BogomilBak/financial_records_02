from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from financial_records_02.api_auth.managers import FinancialRecordsUserManager


class FinancialRecordsUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(default=False)

    objects = FinancialRecordsUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
