from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

from glasses.models import Glass

import os

class GlassDeleteTests(TestCase):

    glass = None

    def get_image(self):
        path = os.path.join(settings.BASE_DIR, 'glasses/static/glasses/images/test_image.jpg')
        return SimpleUploadedFile(
            name='test_image.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg'
        )

    def create_glass(self):
        self.glass = Glass.objects.create(
            name="Glass",
            amount="2",
            price="2.99",
            image=self.get_image()
        )
    
    def test_page_status_code_found(self):
        self.create_glass()
        response = self.client.get(reverse("glass_delete", args=(self.glass.id,)))
        self.assertEquals(response.status_code, 200)

    def test_page_status_code_not_found(self):
        response = self.client.get(reverse("glass_delete", args=(1000,)))
        self.assertEquals(response.status_code, 404)