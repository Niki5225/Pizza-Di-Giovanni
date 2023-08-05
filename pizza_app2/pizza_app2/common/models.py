from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.models import ContentType

from pizza_app2.products.models import Pizza, Drink, CreateYourOwnPizza

UserModel = get_user_model()


class ProductBasketPizza(models.Model):
    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    product = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class ProductBasketOwnPizza(models.Model):
    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    product = models.ForeignKey(
        CreateYourOwnPizza,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class ProductBasketDrink(models.Model):
    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    product = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
