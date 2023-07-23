from django.urls import path
from pizza_app2.products.views import PizzaDetailsView

urlpatterns = (
    path('details/<int:pk>/', PizzaDetailsView.as_view(), name='pizza details'),
)
