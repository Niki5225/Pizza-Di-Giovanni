from django.urls import path, include
from pizza_app2.products.views import pizza_details_view, EditPizzaView, DeletePizzaView, CreateYourOwnPizzaView, \
    CreateYourOwnPizzaEdit, CreateYourOwnPizzaDelete, create_your_own_pizza_details, created_pizzas_by_user

urlpatterns = (
    path('details/<int:pk>/', pizza_details_view, name='pizza details'),
    path('edit/<int:pk>/', EditPizzaView.as_view(), name='pizza edit'),
    path('delete/<int:pk>/', DeletePizzaView.as_view(), name='pizza delete'),
    path('user-pizzas/', include([
        path('', created_pizzas_by_user, name='user-pizzas'),
        path('create/', CreateYourOwnPizzaView.as_view(), name='create your own pizza'),
        path('edit/<int:pk>', CreateYourOwnPizzaEdit.as_view(), name='create your own pizza edit'),
        path('delete/<int:pk>', CreateYourOwnPizzaDelete.as_view(), name='create your own pizza delete'),
        path('details/<int:pk>', create_your_own_pizza_details, name='create your own pizza details')
    ])),
)
