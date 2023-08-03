from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class TestCaseBase(TestCase):

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user
