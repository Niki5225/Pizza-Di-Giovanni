from django.contrib.auth import get_user_model
from django.db import models

# products.models

UserModel = get_user_model()


# Create your models here.

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

    has_tomato_sauce = models.BooleanField(
        null=True,
        blank=True,
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

    image = models.URLField(
        null=False,
        blank=False,
    )

    user_pk = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


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