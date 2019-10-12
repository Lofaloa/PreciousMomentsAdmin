from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from glasses.models import Glass

class GlassCreateTests(TestCase):

    url = '/glasses/create/'

    def test_page_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('glass_create'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_expected_template(self):
        response = self.client.get(reverse('glass_create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'glasses/glass_create.html')