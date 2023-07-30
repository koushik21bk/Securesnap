from django.test import TestCase
from django.urls import reverse
from photos.forms import ImageUploadForm


class TestImageViews(TestCase):
    def test_upload_url_at_desired_location(self):
        response = self.client.get('/photos/upload/')
        self.assertEqual(response.status_code, 200)

    def test_upload_view_accessible_by_name(self):
        response = self.client.get(reverse('photos:upload'))
        self.assertEqual(response.status_code, 200)

    def test_upload_view_uses_correct_template(self):
        response = self.client.get(reverse('photos:upload'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/upload.html')

    def test_upload_view_uses_correct_form(self):
        response = self.client.get(reverse('photos:upload'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ImageUploadForm)
