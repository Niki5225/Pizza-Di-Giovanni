from pizza_app2.products.models import CreateYourOwnPizza


def get_user_pizzas_created(user_pk):
    return CreateYourOwnPizza.objects.filter(user_pk=user_pk)


def get_current_pizza(pk):
    return CreateYourOwnPizza.objects.filter(pk=pk).get()