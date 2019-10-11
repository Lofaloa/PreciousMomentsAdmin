from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

from glasses.models import Glass

import os

class GlassDetailTests(TestCase):

    glass = None

    def get_image(self):
        path = os.path.join(settings.BASE_DIR, 'glasses/static/glasses/images/test_image.jpg')
        return SimpleUploadedFile(
            name='test_image.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg'
        )

    def setUp(self):
        self.glass = Glass.objects.create(
            name="Glass",
            amount="2",
            price="2.99",
            image=self.get_image()
        )
    
    def test_page_status_code_found(self):
        response = self.client.get(reverse("glass_detail", args=(self.glass.id,)))
        self.assertEquals(response.status_code, 200)

    def test_page_status_code_not_found(self):
        response = self.client.get(reverse("glass_detail", args=(1000,)))
        self.assertEquals(response.status_code, 404)

    def test_page_contains_glass_data(self):
        response = self.client.get(reverse("glass_detail", args=(self.glass.id,)))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, self.glass.name)
        self.assertContains(response, self.glass.amount)
        self.assertContains(response, self.glass.price)


    