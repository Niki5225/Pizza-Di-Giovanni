from django.core.exceptions import ValidationError

from pizza_app2.common.utils import get_total_sum


def validate_if_order_is_bigger_than_30_dollars(user_id):
    if get_total_sum(user_id) < 30.00:
        raise ValidationError('The order must be at least 30$ !')
