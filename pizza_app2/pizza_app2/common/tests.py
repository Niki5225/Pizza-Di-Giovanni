from django.core.exceptions import ValidationError
from django.test import TestCase
from pizza_app2.common.validators import min_value_for_order_validator


class OrderValidatorTestCase(TestCase):
    def test_valid_order(self):
        user_id = 1
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_invalid_order(self):
        user_id = 2
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_edge_case(self):
        user_id = 3
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_zero_order(self):
        user_id = 4
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_negative_order(self):
        user_id = 5
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_nonexistent_user(self):
        user_id = 6
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)
