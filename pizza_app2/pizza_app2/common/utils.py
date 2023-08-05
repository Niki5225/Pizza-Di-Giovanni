from pizza_app2.common.models import ProductBasketPizza, ProductBasketOwnPizza, ProductBasketDrink
from pizza_app2.products.models import Pizza, Drink, CreateYourOwnPizza


def get_products_pks(user, objs):
    objects = objs.objects.filter(user_id=user.id).all()
    products_pks = [obj.product_id for obj in objects]
    return products_pks


def get_user_drinks(user, objs):
    product_pks = get_products_pks(user, objs)
    products = []
    for product_pk in product_pks:
        products.append(Drink.objects.filter(pk=product_pk).get())
    return products


def get_user_own_pizzas(user, objs):
    product_pks = get_products_pks(user, objs)
    products = []
    for product_pk in product_pks:
        products.append(CreateYourOwnPizza.objects.filter(pk=product_pk).get())
    return products


def get_user_products_pizzas(user, objs):
    product_pks = get_products_pks(user, objs)
    products = []
    for product_pk in product_pks:
        products.append(Pizza.objects.filter(pk=product_pk).get())
    return products


def get_total_sum(user_id):
    total_sum = 0

    for obj in ProductBasketPizza.objects.filter(user_id=user_id):
        total_sum += obj.product.price

    for obj in ProductBasketOwnPizza.objects.filter(user_id=user_id):
        total_sum += obj.product.price

    for obj in ProductBasketDrink.objects.filter(user_id=user_id):
        total_sum += obj.product.price

    return total_sum
