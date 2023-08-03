from django.urls import path

from pizza_app2.common.views import IndexView, PizzasOfferedView, DrinksOfferedView, add_to_basket, ProductsBasketView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('pizzas/', PizzasOfferedView.as_view(), name='pizzas-offered'),
    path('drinks/', DrinksOfferedView.as_view(), name='drinks-offered'),
    path('basket/', ProductsBasketView.as_view(), name='basket-view'),
    path('add_to_basket/<str:product_type>/<int:pk>/', add_to_basket, name='add_to_basket'),
)
