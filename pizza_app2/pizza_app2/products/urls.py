from django.urls import path
from pizza_app2.products.views import pizza_details_view, EditPizzaView, DeletePizzaView

urlpatterns = (
    path('details/<int:pk>/', pizza_details_view, name='pizza details'),
    path('edit/<int:pk>/', EditPizzaView.as_view(), name='pizza edit'),
    path('delete/<int:pk>/', DeletePizzaView.as_view(), name='pizza delete'),
)
