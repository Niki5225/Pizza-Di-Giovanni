from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic as views

from pizza_app2.products.models import Pizza
from pizza_app2.products.utils import get_user_pizzas_created


# Create your views here.


class IndexView(views.TemplateView):
    template_name = 'index.html'


class PizzasOfferedView(views.TemplateView):
    template_name = 'products/products-offered.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_pizzas_offered'] = Pizza.objects.all()

        return context


@login_required
def created_pizzas_by_user(request):
    context = {
        'pizzas_created_by_the_user': get_user_pizzas_created(request.user.pk),
    }

    return render(request, 'products/created-pizzas-by-user.html', context)
