from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.filter
def get_content_type_id(model):
    content_type = ContentType.objects.get_for_model(model)
    return content_type.id
