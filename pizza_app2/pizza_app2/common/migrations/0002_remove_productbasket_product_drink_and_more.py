# Generated by Django 4.2 on 2023-08-04 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbasket',
            name='product_drink',
        ),
        migrations.RemoveField(
            model_name='productbasket',
            name='product_own_pizza',
        ),
        migrations.RemoveField(
            model_name='productbasket',
            name='product_pizza',
        ),
        migrations.RemoveField(
            model_name='productbasket',
            name='quantity',
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.productbasket')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddField(
            model_name='productbasket',
            name='items',
            field=models.ManyToManyField(to='common.basketitem'),
        ),
    ]
