from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views

from pizza_app2.accounts.models import AppUser


# Create your views here.

class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-view.html'
    model = AppUser


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-view.html'


class LogoutUserView(auth_views.LogoutView):
    template_name = 'accounts/logout-view.html'