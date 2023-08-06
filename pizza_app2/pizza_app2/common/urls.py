from django.urls import path

from pizza_app2.common.views import IndexView, PizzasOfferedView, DrinksOfferedView, ProductsBasketView, \
    add_product_to_basket_pizza, add_product_to_basket_own_pizza, add_product_to_basket_drink, order, \
    reduce_quantity_of_product_in_basket_drink, reduce_quantity_of_product_in_basket_pizza, \
    reduce_quantity_of_product_in_basket_own_pizza

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('pizzas/', PizzasOfferedView.as_view(), name='pizzas-offered'),
    path('drinks/', DrinksOfferedView.as_view(), name='drinks-offered'),
    path('basket/', ProductsBasketView.as_view(), name='basket-view'),
    path('add-pizza-to-basket/<int:pk>/', add_product_to_basket_pizza, name='add-pizza-to-basket'),
    path('add-own-pizza-to-basket/<int:pk>/', add_product_to_basket_own_pizza, name='add-own-pizza-to-basket'),
    path('add-drink-to-basket/<int:pk>/', add_product_to_basket_drink, name='add-drink-to-basket'),
    path('reduce-pizza-from-basket/<int:pk>/', reduce_quantity_of_product_in_basket_pizza,
         name='reduce-pizza-from-basket'),
    path('reduce-own-pizza-from-basket/<int:pk>/', reduce_quantity_of_product_in_basket_own_pizza,
         name='reduce-own-pizza-from-basket'),
    path('reduce-drink-from-basket/<int:pk>/', reduce_quantity_of_product_in_basket_drink,
         name='reduce-drink-from-basket'),
    path('ordered/', order, name='order-made'),
)
