from django import template

register = template.Library()


@register.filter
def placeholder(value, text):
    value.field.widget.attrs['placeholder'] = text

    return value
