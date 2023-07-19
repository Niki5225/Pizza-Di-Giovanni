from django.urls import path

from pizza_app2.common.views import IndexView, ProductsOfferedView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsOfferedView.as_view(), name='products-offered'),
)