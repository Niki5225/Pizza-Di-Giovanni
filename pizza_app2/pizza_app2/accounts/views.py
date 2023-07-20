from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, authenticate, login

from pizza_app2.accounts.forms import RegisterUserForm

# Create your views here.

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-view.html'
    model = UserModel
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object

        login(self.request, user)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-view.html'
    success_url = reverse_lazy('index')
    model = UserModel

class LogoutUserView(auth_views.LogoutView):
    template_name = 'accounts/logout-view.html'
    next_page = reverse_lazy('index')


class DeleteUserView(views.DeleteView):
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(*args, **kwargs)

        return response


class EditUserView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/edit-profile.html'
    success_url = reverse_lazy('details user')


class DetailsUserView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel


