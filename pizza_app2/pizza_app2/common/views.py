from django.views import generic as views
from pizza_app2.products.models import Pizza


class IndexView(views.TemplateView):
    template_name = 'index.html'


class PizzasOfferedView(views.TemplateView):
    template_name = 'products/products-offered.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_pizzas_offered'] = Pizza.objects.all()

        return context
