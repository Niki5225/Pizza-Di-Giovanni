# Generated by Django 4.2 on 2023-08-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_appuser_phone_number_alter_appuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='address',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]