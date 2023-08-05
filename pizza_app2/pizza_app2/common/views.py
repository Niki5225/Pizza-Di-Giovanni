from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic as views
from pizza_app2.common.models import ProductBasketPizza, ProductBasketOwnPizza, ProductBasketDrink
from pizza_app2.common.utils import get_user_products_pizzas, get_total_sum
from pizza_app2.common.validators import validate_if_order_is_bigger_than_30_dollars
from pizza_app2.products.models import Pizza, Drink


class IndexView(views.TemplateView):
    template_name = 'index.html'


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
def order(request):
    user_basket_products_pizza = ProductBasketPizza.objects.filter(user_id=request.user.pk)
    user_basket_products_own_pizza = ProductBasketOwnPizza.objects.filter(user_id=request.user.pk)
    user_basket_products_drink = ProductBasketDrink.objects.filter(user_id=request.user.pk)

    if user_basket_products_pizza or user_basket_products_own_pizza or user_basket_products_drink:
        validate_if_order_is_bigger_than_30_dollars(request.user.pk)
        for obj in user_basket_products_pizza:
            ProductBasketPizza.objects.get(product_id=obj.product_id, user_id=request.user.pk).delete()
        for obj2 in user_basket_products_own_pizza:
            ProductBasketOwnPizza.objects.get(product_id=obj2.product_id, user_id=request.user.pk).delete()
        for obj3 in user_basket_products_drink:
            ProductBasketDrink.objects.get(product_id=obj3.product_id, user_id=request.user.pk).delete()
        return redirect('order-made')
    return redirect('pizzas-offered')
