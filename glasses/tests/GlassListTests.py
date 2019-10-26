from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from glasses.models import Glass

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

import os

class GlassListTests(TestCase):

    url = "/glasses/"

    def get_image(self):
        path = os.path.join(settings.BASE_DIR, 'glasses/static/glasses/images/test_image.jpg')
        return SimpleUploadedFile(
            name='test_image.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg'
        )

    def test_page_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('glass_list'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_expected_template(self):
        response = self.client.get(reverse('glass_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'glasses/glass_list.html')

    def test_page_expected_content_without_glasses(self):
        response = self.client.get('/glasses/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h2>C'est un peu vide ici!</h2>")
        self.assertContains(response, (
            "<p>Vous n'avez pas de réalisations. Commencez votre collection en"
            " cliquant sur le bouton \"<i>Nouvelle réalisation</i>\".</p>"
        ))

    def test_page_expected_content_with_glasses(self):
        glass = Glass(name='Glass', amount='2', price='2.99', image=self.get_image())
        glass.save()
        response = self.client.get('/glasses/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "<h2>C'est un peu vide ici!</h2>")
        self.assertNotContains(response, (
            "<p>Vous n'avez pas de réalisations. Commencez votre collection en"
            " cliquant sur le bouton \"<i>Nouvelle réalisation</i>\".</p>"
        ))
        self.assertContains(response, "<h5 class=\"card-title\">Glass</h5>")
        self.assertContains(response, (
            "<p class=\"card-text\">2.99€ (2 paires "
            "disponibles)</p>"
        ))