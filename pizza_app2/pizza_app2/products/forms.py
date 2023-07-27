from django import forms

from pizza_app2.products.models import CreateYourOwnPizza


class CreateYourOwnPizzaBaseForm(forms.ModelForm):
    class Meta:
        model = CreateYourOwnPizza
        fields = ('pizza_name', 'has_cheese', 'topping', 'dough', 'image')

        labels = {
            'pizza_name': 'Pizza Name',
            'has_cheese': 'Cheese Type',
            'dough': 'Dough Type',
            'image': 'Image',
        }

        widgets = {
            'pizza_name': forms.TextInput(attrs={'placeholder': 'Enter your pizza name'}),
            'image': forms.TextInput(attrs={'placeholder': 'Place your valid URL'}),
        }


class CreateYourOwnPizzaForm(CreateYourOwnPizzaBaseForm):
    pass


class CreateYourOwnPizzaEditForm(CreateYourOwnPizzaBaseForm):
    pass
