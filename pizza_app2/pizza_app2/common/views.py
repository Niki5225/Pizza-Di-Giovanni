from django.shortcuts import render
from django.views import generic as views


# Create your views here.


class IndexView(views.TemplateView):
    template_name = 'index.html'


class ProductsOfferedView(views.TemplateView):
    template_name = 'products/products-offered.html'
