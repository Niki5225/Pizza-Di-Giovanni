# Generated by Django 4.2 on 2023-08-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_createyourownpizza_user_pk'),
        ('common', '0006_rename_productbasket_productbasketpizza_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbasketownpizza',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.createyourownpizza'),
        ),
    ]
