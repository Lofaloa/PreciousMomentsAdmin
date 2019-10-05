from django.test import TestCase
from glasses.models import Glass

from django.core.files.uploadedfile import SimpleUploadedFile

class GlassIndexViewTests(TestCase):

    def test_no_glasses(self):
        """
        If no glasses exist, an appropriate message is displayed.
        """
        response = self.client.get('/glasses/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucunes réalisations.")

    def test_create_new_glass(self):
        """
        When a glass is created and saved, it should be saved in the database
        in an expected state.
        """
        pass