# Generated by Django 4.2 on 2023-08-05 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_alter_createyourownpizza_user_pk'),
        ('common', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbasket',
            name='items',
        ),
        migrations.RemoveField(
            model_name='productbasket',
            name='session_id',
        ),
        migrations.AddField(
            model_name='productbasket',
            name='product',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='products.pizza'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productbasket',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productbasket',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BasketItem',
        ),
    ]
