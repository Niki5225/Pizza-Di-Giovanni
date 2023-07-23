from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.views.decorators.cache import cache_page
from pizza_app2.products.models import Pizza
from pizza_app2.settings import CACHE_TTL


# Create your views here.


class PizzaDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'products/pizza-details.html'
    model = Pizza

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pizza'] = Pizza.objects.get(pk=self.object.pk)

        return context
