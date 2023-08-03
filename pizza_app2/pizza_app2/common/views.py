from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic as views
from pizza_app2.common.models import ProductBasket
from pizza_app2.common.utils import sum_total_checkout_price, get_user_pizzas, get_user_drinks, get_user_own_pizzas
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
    model = ProductBasket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_basket'] = ProductBasket.objects.filter(user_id=self.request.user.pk)
        context['total_sum'] = sum_total_checkout_price(self.request.user.pk)
        context['products_pizzas'] = get_user_pizzas(self.request.user, ProductBasket)
        context['products_created_pizzas'] = get_user_own_pizzas(self.request.user, ProductBasket)
        context['products_drinks'] = get_user_drinks(self.request.user, ProductBasket)

        return context


@login_required
def add_to_basket(request, product_type, pk):
    # product = None
    # if product_type == 'pizza':
    #     product = Pizza.objects.filter(pk=pk).get()
    # elif product_type == 'create_your_own_pizza':
    #     product = CreateYourOwnPizza.objects.filter(pk=pk).get()
    # elif product_type == 'drink':
    #     product = Drink.objects.filter(pk=pk).get()

    user_basket_product = ProductBasket.objects \
        .filter(product_id=pk, user_id=request.user.pk, product_type=product_type)

    if not user_basket_product:
        ProductBasket.objects.create(
            product_id=pk,
            user_id=request.user.pk,
            quantity=1
        )
    else:
        current_product = user_basket_product.get(product_id=pk, product_type=product_type)
        current_product.quantity += 1
        current_product.save()

    return redirect('basket_view')
