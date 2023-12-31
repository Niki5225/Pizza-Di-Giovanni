# Generated by Django 4.2 on 2023-08-03 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0010_alter_createyourownpizza_user_pk'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product_drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
                ('product_own_pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.createyourownpizza')),
                ('product_pizza', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
