from django.core.management import call_command
from django.test import TestCase

from user.models import CustomUser


class TestCustomUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command("loaddata", "fixtures/fixtures.json", verbosity=0)

    def test_custom_user_str(self):
        user = CustomUser.objects.get(pk=1)
        expected_data = user.email
        self.assertEqual(expected_data, str(user))
