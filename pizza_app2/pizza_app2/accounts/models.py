from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from pizza_app2.accounts.custom_validators import validate_only_letters


# Create your models here.


class AppUser(auth_models.AbstractUser):
    FIRST_NAME_MAX_LEN = 40
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 40
    LAST_NAME_MIN_LEN = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    address = models.CharField(
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
