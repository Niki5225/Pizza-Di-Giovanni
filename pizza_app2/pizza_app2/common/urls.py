from django.urls import path

from pizza_app2.common.views import IndexView, PizzasOfferedView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('pizzas/', PizzasOfferedView.as_view(), name='products-offered'),

)
