from django.test import TestCase
from utils.tests.models import TestModel
from user.models import User


class TestUserModelFields(TestCase):
    """This class tests field of the user model"""

    # Test verbose names
    def test_first_name_verbose_name(self):
        label = TestModel.get_verbose_name(User, "first_name")
        self.assertEqual(label, "first name")

    def test_last_name_verbose_name(self):
        label = TestModel.get_verbose_name(User, "last_name")
        self.assertEqual(label, "last name")

    def test_username_verbose_name(self):
        label = TestModel.get_verbose_name(User, "username")
        self.assertEqual(label, "username")

    def test_email_verbose_name(self):
        label = TestModel.get_verbose_name(User, "email")
        self.assertEqual(label, "email address")

    def test_password_verbose_name(self):
        label = TestModel.get_verbose_name(User, "password")
        self.assertEqual(label, "password")

    # Test max length
    def test_first_name_max_len(self):
        max_len = TestModel.get_max_length(User, "first_name")
        self.assertEqual(max_len, 150)

    def test_last_name_max_len(self):
        max_len = TestModel.get_max_length(User, "last_name")
        self.assertEqual(max_len, 150)

    def test_username_max_len(self):
        max_len = TestModel.get_max_length(User, "username")
        self.assertEqual(max_len, 150)

    def test_email_max_len(self):
        max_len = TestModel.get_max_length(User, "email")
        self.assertEqual(max_len, 254)

    def test_password_max_len(self):
        max_len = TestModel.get_max_length(User, "password")
        self.assertEqual(max_len, 128)
