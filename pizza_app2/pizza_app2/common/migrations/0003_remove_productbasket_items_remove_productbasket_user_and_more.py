# Generated by Django 4.2 on 2023-08-05 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_productbasket_product_drink_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbasket',
            name='items',
        ),
        migrations.RemoveField(
            model_name='productbasket',
            name='user',
        ),
        migrations.DeleteModel(
            name='BasketItem',
        ),
        migrations.DeleteModel(
            name='ProductBasket',
        ),
    ]