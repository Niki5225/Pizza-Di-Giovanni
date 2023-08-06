from django.core.exceptions import ValidationError

from pizza_app2.common.utils import get_total_sum


def min_value_for_order_validator(user_id):
    if get_total_sum(user_id) < 30.00:
        raise ValidationError('The order must be at least 30$ !')
