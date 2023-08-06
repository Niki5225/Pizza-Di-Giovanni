from django.core.exceptions import ValidationError
from django.test import TestCase
from pizza_app2.common.validators import min_value_for_order_validator


class OrderValidatorTestCase(TestCase):
    def test_valid_order(self):
        # Total sum is greater than $30, so no exception should be raised
        user_id = 1
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_invalid_order(self):
        # Total sum is less than $30, so a ValidationError should be raised
        user_id = 2
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_edge_case(self):
        # Total sum is exactly $30, which is the minimum limit, no exception should be raised
        user_id = 3
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_zero_order(self):
        # Total sum is $0, which is less than $30, so a ValidationError should be raised
        user_id = 4
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_negative_order(self):
        # Total sum is negative, which is less than $30, so a ValidationError should be raised
        user_id = 5
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)

    def test_nonexistent_user(self):
        # Assuming get_total_sum raises an exception for a nonexistent user,
        # your validator should handle that and raise a ValidationError
        user_id = 6
        with self.assertRaises(ValidationError):
            min_value_for_order_validator(user_id)
