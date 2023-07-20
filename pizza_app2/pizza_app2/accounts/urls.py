# accounts.urls
from django.urls import path

from pizza_app2.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, EditUserView, DeleteUserView, \
    DetailsUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('edit', EditUserView.as_view(), name='edit user'),
    path('delete', DeleteUserView.as_view(), name='delete user'),
    path('details/<int:pk>/', DetailsUserView.as_view(), name='details user'),
)
