from django.test import TestCase
from django.contrib.auth import get_user_model
from pizza_app2.accounts.custom_validators import validate_only_letters

UserModel = get_user_model()


class TestCaseBase(TestCase):

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user


class OnlyLettersValidator(TestCase):

    def test_only_letters_validator_when_given_data_valid(self):
        validate_only_letters('abcdABCD')

    def test_only_letters_validator_when_given_data_is_none(self):
        validate_only_letters('')

    def test_only_letters_validator_when_given_data_contains_numbers_expect_error(self):
        with self.assertRaises(Exception) as context:
            validate_only_letters('abcde1234abcd')

        self.assertIsNotNone(context.exception)

    def test_only_letters_validator_when_given_data_contains_special_characters_expect_error(self):
        with self.assertRaises(Exception) as context:
            validate_only_letters('abcde@#$%abcd')

        self.assertIsNotNone(context.exception)
