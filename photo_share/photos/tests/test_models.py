from django.test import TestCase
from utils.tests.models import TestModel
from photos.models import Image


class TestImageFields(TestCase):
    """This class tests image model fields"""

    def test_name_varbose_name(self):
        label = TestModel.get_verbose_name(Image, 'name')
        self.assertEqual(label, 'name')

    def test_image_verbose_name(self):
        label = TestModel.get_verbose_name(Image, 'image')
        self.assertEqual(label, 'image')

    def test_status_verbose_name(self):
        label = TestModel.get_verbose_name(Image, 'status')
        self.assertEqual(label, 'status')

    def test_name_max_length(self):
        max_len = TestModel.get_max_length(Image, 'name')
        self.assertEqual(max_len, 150)

    def test_status_max_length(self):
        max_len = TestModel.get_max_length(Image, 'status')
        self.assertEqual(max_len, 7)

    def test_name_unique(self):
        field = TestModel.get_field(Image, 'name').unique
        self.assertEqual(field, True)
