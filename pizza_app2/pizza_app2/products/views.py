from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from pizza_app2.products.forms import CreateYourOwnPizzaForm, CreateYourOwnPizzaEditForm
from pizza_app2.products.models import Pizza, CreateYourOwnPizza
from django.views import generic as views

from pizza_app2.products.utils import get_user_pizzas_created, get_current_pizza


@login_required
def pizza_details_view(request, pk):
    product = Pizza.objects.filter(pk=pk).get()

    request.session.set_expiry(0)

    last_seen_product_lst = request.session.get('last_seen_product_id', [])

    last_seen_product_lst.append(product.pk)

    if len(last_seen_product_lst) == 1:
        prev_product_id = last_seen_product_lst[0]
    else:
        prev_product_id = last_seen_product_lst[-2]

    # Only in cases while there is changes in the main menu, you can use this scenario to do not throw any errors.
    # Example - you just deleted a pizza from the menu, but some user's last seen product is that concrete pizza

    # if Pizza.objects.filter(pk=prev_product_id).exists():
    #     prev_product = Pizza.objects.filter(pk=prev_product_id).get()
    # else:
    #     prev_product = product

    request.session['last_seen_product_id'] = last_seen_product_lst

    context = {
        'pizza': product,
        'prev_product_id': prev_product_id,
        'prev_product': Pizza.objects.filter(pk=prev_product_id).get(),  # Here you put the 'prev_product'
    }

    return render(request, 'products/pizza-details.html', context)


@login_required
def created_pizzas_by_user(request):
    context = {
        'pizzas_created_by_the_user': get_user_pizzas_created(request.user.pk),
    }

    return render(request, 'products/created-pizzas-by-user.html', context)


class EditPizzaView(LoginRequiredMixin, views.UpdateView):
    template_name = 'products/pizza-edit.html'
    model = Pizza
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('pizza details', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pizza'] = self.object

        return context


class DeletePizzaView(LoginRequiredMixin, views.DeleteView):
    template_name = 'products/pizza-delete.html'
    model = Pizza
    success_url = reverse_lazy('products-offered')


class CreateYourOwnPizzaView(LoginRequiredMixin, views.CreateView):
    model = CreateYourOwnPizza
    template_name = 'products/create-your-own-pizza.html'
    form_class = CreateYourOwnPizzaForm

    def form_valid(self, form):
        form.instance.user_pk = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user-pizzas')


# class CreateYourOwnPizzaDetails(LoginRequiredMixin, views.DetailView):
#     template_name = 'products/create-your-own-pizza-details.html'
#     model = CreateYourOwnPizza
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['current_pizza'] = self.object.pk
#
#         return context

def create_your_own_pizza_details(request, pk):
    context = {
        'current_pizza': get_current_pizza(pk),
    }

    return render(request, 'products/create-your-own-pizza-details.html', context)


class CreateYourOwnPizzaEdit(LoginRequiredMixin, views.UpdateView):
    template_name = 'products/create-your-own-pizza-edit.html'
    model = CreateYourOwnPizza
    form_class = CreateYourOwnPizzaEditForm

    def get_success_url(self):
        return reverse_lazy('create your own pizza details', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pizza'] = self.object

        return context


class CreateYourOwnPizzaDelete(LoginRequiredMixin, views.DeleteView):
    model = CreateYourOwnPizza
    template_name = 'products/create-your-own-pizza-delete.html'
    success_url = reverse_lazy('user-pizzas')
