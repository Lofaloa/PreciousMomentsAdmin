from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.conf import settings
from glasses.forms import GlassModelForm
import os

class GlassModelFormTests(TestCase):

    def create_test_image(self):
        """
        Creates an image used to simulate an image uploaded by a user.
        """
        image_path = os.path.join(settings.MEDIA_ROOT, 'images/test_image.png')
        return SimpleUploadedFile(
            name='test_image.png',
            content=open(image_path, 'rb').read(),
            content_type='image/png'
        )

    def create_glass_form(self, name, amount, price):
        """
        Creates a form with the specified data and a test image.
        """
        form_data = {
            'name': name,
            'amount': amount,
            'price': price,
            'image': self.create_test_image()
        }
        return GlassModelForm(form_data)

    def test_image_creation(self):
        image= self.create_test_image()
        self.assertIsNotNone(image)

    def test_valid_data(self):
        """
        The form should be valid when all the specified data are valid.
        """
        form = self.create_glass_form(
            'Verre à tournesol',
            '5',
            '4.99'
        )
        self.assertTrue(form.is_valid())

    def test_null_glass_name(self):
        """
        The form should not be valid when the glass name is null (None).
        """
        form = self.create_glass_form(
            None,
            '5',
            '4.99'
        )
        self.assertFalse(form.is_valid())

    def test_blank_glass_name(self):
        """
        The form should not be valid when the glass name is blank.
        """
        form = self.create_glass_form(
            '',
            '5',
            '4.99'
        )
        self.assertFalse(form.is_valid())

    def test_negative_amount(self):
        """
        The form should not be valid when the amount of glasses is negative.
        """
        form = self.create_glass_form(
            'Verre à tournesol',
            '-5',
            '4.99'
        )
        self.assertFalse(form.is_valid())

    def test_negative_price(self):
        """
        The form should not be valid when the price of a glass is negative.
        """
        form = self.create_glass_form(
            'Verre à tournesol',
            '5',
            '-4.99'
        )
        self.assertFalse(form.is_valid())