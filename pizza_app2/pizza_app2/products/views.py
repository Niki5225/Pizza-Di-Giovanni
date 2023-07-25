from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from pizza_app2.products.models import Pizza
from django.views import generic as views


@login_required
def pizza_details_view(request, pk):
    product = Pizza.objects.filter(pk=pk).get()

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
        'prev_product': Pizza.objects.filter(pk=prev_product_id).get(),
    }

    return render(request, 'products/pizza-details.html', context)


class EditPizzaView(LoginRequiredMixin, views.UpdateView):
    template_name = 'products/pizza-edit.html'
    model = Pizza
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('pizza details', kwargs={
            'pk': Pizza.objects.filter(pk=self.object.pk),
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pizza'] = self.object.pk

        return context


class DeletePizzaView(LoginRequiredMixin, views.DeleteView):
    template_name = 'products/pizza-delete.html'
    model = Pizza
    success_url = reverse_lazy('products-offered')
