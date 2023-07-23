from pizza_app2.products.models import CreateYourOwnPizza


def get_user_pizzas_created(user_pk):
    return CreateYourOwnPizza.objects.filter(user_pk=user_pk)
