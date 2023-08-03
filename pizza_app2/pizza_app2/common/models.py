from django.contrib.auth import get_user_model
from django.db import models

from pizza_app2.products.models import Pizza, Drink, CreateYourOwnPizza

UserModel = get_user_model()


class ProductBasket(models.Model):
    ordering = ('quantity',)

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    product_pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    product_own_pizza = models.ForeignKey(
        CreateYourOwnPizza,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    product_drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
