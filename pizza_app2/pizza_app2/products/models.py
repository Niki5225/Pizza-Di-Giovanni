from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models


UserModel = get_user_model()


class CreateYourOwnPizza(models.Model):
    CHEESE_CHOICES = (
        ('Mozzarella', 'Mozzarella'),
        ('Parmigiano', 'Parmigiano'),
        ('Cottage', 'Cottage'),
        ('Cheddar', 'Cheddar'),
        ('Emmental', 'Emmental')
    )

    DOUGH_CHOICES = (
        ('Neapolitan', 'Neapolitan'),
        ('Gluten Free', 'Gluten Free'),
        ('Sicilian', 'Sicilian'),
        ('Whole Wheat', 'Whole Wheat'),
        ('Dietary', 'Dietary'),
    )

    TOPPING_CHOICES = [
        ('Pepperoni', 'Pepperoni'),
        ('Mushrooms', 'Mushrooms'),
        ('Onions', 'Onions'),
        ('Sausage', 'Sausage'),
        ('Olives', 'Olives'),
    ]

    pizza_name = models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )

    has_cheese = models.CharField(
        choices=CHEESE_CHOICES,
        null=True,
        blank=True,
        max_length=10,
    )

    dough = models.CharField(
        choices=DOUGH_CHOICES,
        null=False,
        blank=False,
        max_length=11,
    )

    topping = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        choices=TOPPING_CHOICES,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    user_pk = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    price = 25


class Pizza(models.Model):
    pizza_name = models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )

    dough = models.CharField(
        null=False,
        blank=False,
        max_length=40,
    )

    tomato_sauce = models.BooleanField(
        null=True,
        blank=True,
    )

    cheese_type = models.CharField(
        null=False,
        blank=False,
        max_length=40,
    )

    meat_type = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )


class Drink(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=40,
    )

    price = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )
