# Generated by Django 4.2.3 on 2023-07-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_appuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
