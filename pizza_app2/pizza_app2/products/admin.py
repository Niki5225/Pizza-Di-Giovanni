from django.contrib import admin

from pizza_app2.products.models import Pizza


# Register your models here.

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass
