from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic as views
from pizza_app2.accounts.models import AppUser
from pizza_app2.common.models import ProductBasketPizza, ProductBasketOwnPizza, ProductBasketDrink
from pizza_app2.common.utils import get_user_products_pizzas, get_total_sum
from pizza_app2.common.validators import min_value_for_order_validator
from pizza_app2.products.models import Pizza, Drink


class IndexView(views.TemplateView):
    template_name = 'common/index.html'


class PizzasOfferedView(views.TemplateView):
    template_name = 'products/pizzas-offered.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_pizzas_offered'] = Pizza.objects.all()

        return context


class DrinksOfferedView(views.TemplateView):
    template_name = 'products/drinks-offered.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_drinks_offered'] = Drink.objects.all()

        return context


class ProductsBasketView(LoginRequiredMixin, views.ListView):
    template_name = 'common/basket.html'
    model = ProductBasketPizza

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizza_basket'] = ProductBasketPizza.objects.filter(user_id=self.request.user.pk)
        context['own_pizza_basket'] = ProductBasketOwnPizza.objects.filter(user_id=self.request.user.pk)
        context['drink_basket'] = ProductBasketDrink.objects.filter(user_id=self.request.user.pk)
        context['total_sum'] = get_total_sum(self.request.user.pk)
        context['products'] = get_user_products_pizzas(self.request.user, ProductBasketPizza)

        return context


@login_required
def add_product_to_basket_pizza(request, pk):
    user_basket_product = ProductBasketPizza.objects.filter(product_id=pk, user_id=request.user.pk)

    if not user_basket_product:
        ProductBasketPizza.objects.create(
            product_id=pk,
            user_id=request.user.pk,
            quantity=1
        )
    else:
        current_product = ProductBasketPizza.objects.get(product_id=pk)
        current_product.quantity += 1
        current_product.save()

    return redirect('basket-view')


@login_required
def add_product_to_basket_own_pizza(request, pk):
    user_basket_product = ProductBasketOwnPizza.objects.filter(product_id=pk, user_id=request.user.pk)

    if not user_basket_product:
        ProductBasketOwnPizza.objects.create(
            product_id=pk,
            user_id=request.user.pk,
            quantity=1
        )
    else:
        current_product = ProductBasketOwnPizza.objects.get(product_id=pk)
        current_product.quantity += 1
        current_product.save()

    return redirect('basket-view')


@login_required
def add_product_to_basket_drink(request, pk):
    user_basket_product = ProductBasketDrink.objects.filter(product_id=pk, user_id=request.user.pk)

    if not user_basket_product:
        ProductBasketDrink.objects.create(
            product_id=pk,
            user_id=request.user.pk,
            quantity=1
        )
    else:
        current_product = ProductBasketDrink.objects.get(product_id=pk)
        current_product.quantity += 1
        current_product.save()

    return redirect('basket-view')


@login_required
def reduce_quantity_of_product_in_basket_pizza(request, pk):
    pizza = ProductBasketPizza.objects.filter(pk=pk, user_id=request.user.pk).get()

    if pizza.quantity - 1 == 0:
        remove_product_from_basket_pizza(request, pk)
    else:
        pizza.quantity -= 1
        pizza.save()

    return redirect('basket-view')


@login_required
def reduce_quantity_of_product_in_basket_own_pizza(request, pk):
    own_pizza = ProductBasketOwnPizza.objects.filter(pk=pk, user_id=request.user.pk).get()

    if own_pizza.quantity - 1 == 0:
        remove_product_from_basket_own_pizza(request, pk)
    else:
        own_pizza.quantity -= 1
        own_pizza.save()

    return redirect('basket-view')


@login_required
def reduce_quantity_of_product_in_basket_drink(request, pk):
    drink = ProductBasketDrink.objects.filter(pk=pk, user_id=request.user.pk).get()

    if drink.quantity - 1 == 0:
        remove_product_from_basket_drink(request, pk)
    else:
        drink.quantity -= 1
        drink.save()

    return redirect('basket-view')


@login_required
def increase_quantity_of_product_in_basket_pizza(request, pk):
    pizza = ProductBasketPizza.objects.filter(pk=pk, user_id=request.user.pk).get()

    pizza.quantity += 1
    pizza.save()

    return redirect('basket-view')


@login_required
def increase_quantity_of_product_in_basket_own_pizza(request, pk):
    own_pizza = ProductBasketOwnPizza.objects.filter(pk=pk, user_id=request.user.pk).get()

    own_pizza.quantity += 1
    own_pizza.save()

    return redirect('basket-view')


@login_required
def increase_quantity_of_product_in_basket_drink(request, pk):
    drink = ProductBasketDrink.objects.filter(pk=pk, user_id=request.user.pk).get()

    drink.quantity += 1
    drink.save()

    return redirect('basket-view')


@login_required
def remove_product_from_basket_pizza(request, pk):
    pizza = ProductBasketPizza.objects.filter(pk=pk, user_id=request.user.pk).get()
    if pizza:
        pizza.delete()
    return redirect('basket-view')


@login_required
def remove_product_from_basket_own_pizza(request, pk):
    own_pizza = ProductBasketOwnPizza.objects.filter(pk=pk, user_id=request.user.pk).get()
    if own_pizza:
        own_pizza.delete()
    return redirect('basket-view')


@login_required
def remove_product_from_basket_drink(request, pk):
    drink = ProductBasketDrink.objects.filter(pk=pk, user_id=request.user.pk).get()
    if drink:
        drink.delete()
    return redirect('basket-view')


@login_required
def order(request):
    user_basket_products_pizza = ProductBasketPizza.objects.filter(user_id=request.user.pk)
    user_basket_products_own_pizza = ProductBasketOwnPizza.objects.filter(user_id=request.user.pk)
    user_basket_products_drink = ProductBasketDrink.objects.filter(user_id=request.user.pk)

    if user_basket_products_pizza or user_basket_products_own_pizza or user_basket_products_drink:
        min_value_for_order_validator(request.user.pk)
        for obj in user_basket_products_pizza:
            ProductBasketPizza.objects.get(product_id=obj.product_id, user_id=request.user.pk).delete()
        for obj2 in user_basket_products_own_pizza:
            ProductBasketOwnPizza.objects.get(product_id=obj2.product_id, user_id=request.user.pk).delete()
        for obj3 in user_basket_products_drink:
            ProductBasketDrink.objects.get(product_id=obj3.product_id, user_id=request.user.pk).delete()

        context = {
            'user': AppUser.objects.filter(pk=request.user.pk).get(),
        }
        return render(request, 'common/order-made.html', context)
    return redirect('pizzas-offered')


# class Shape:
#
#     def area(self):
#         return 5
#
#
# class Triangle(Shape):
#
#     def
