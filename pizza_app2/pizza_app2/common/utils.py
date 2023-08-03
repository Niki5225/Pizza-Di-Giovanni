from pizza_app2.common.models import ProductBasket
from pizza_app2.products.models import Pizza, Drink, CreateYourOwnPizza


def sum_total_checkout_price(user_pk):
    user_basket = ProductBasket.objects.filter(user_id=user_pk)
    total = 0
    for product in user_basket:
        total += product.quantity * product.product.price
    return total


def get_products_pks(user, objs):
    objects = objs.objects.filter(user_id=user.id).all()
    products_pks = [obj.product_id for obj in objects]
    return products_pks


def get_user_pizzas(user, objs):
    product_pks = get_products_pks(user, objs)
    products = []
    for product_pk in product_pks:
        products.append(Pizza.objects.filter(pk=product_pk).get())
    return products


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
