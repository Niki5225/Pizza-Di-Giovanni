# accounts.urls
from django.urls import path

from pizza_app2.accounts.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
)