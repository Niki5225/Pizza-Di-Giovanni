from django.urls import path

from pizza_app2.common.views import IndexView, PizzasOfferedView, created_pizzas_by_user

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('pizzas/', PizzasOfferedView.as_view(), name='products-offered'),
    path('user-pizzas/', created_pizzas_by_user, name='user-pizzas'),
)
