from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.test import TestCase, override_settings
from django.conf import settings

from glasses.forms.glass_create_form import GlassCreateForm

import os

class GlassCreateFormTests(TestCase):

    def get_image(self):
        path = os.path.join(settings.BASE_DIR, 'glasses/static/glasses/images/test_image.jpg')
        return SimpleUploadedFile(
            name='test_image.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg'
        )

    def create_glass_form(self, name, amount, price):
        form_data = {'name': name, 'amount': amount, 'price': price}
        return GlassCreateForm(
            data=form_data, 
            files={'image': self.get_image()}
        )

    def test_valid_glass(self):
        form = self.create_glass_form(
            'Verre',
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
        self.assertIsNotNone(form.errors.as_data()['name'])

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
        self.assertIsNotNone(form.errors.as_data()['name'])

    def test_null_amount(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            None,
            '4.99'
        )
        self.assertFalse(form.is_valid())
        self.assertIsNotNone(form.errors.as_data()['amount'])

    def test_blank_amount(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            '',
            '4.99'
        )
        self.assertFalse(form.is_valid())
        self.assertIsNotNone(form.errors.as_data()['amount'])

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
        self.assertIsNotNone(form.errors.as_data()['amount'])

    def test_null_price(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            '5',
            None
        )
        self.assertFalse(form.is_valid())
        self.assertIsNotNone(form.errors.as_data()['price'])

    def test_blank_price(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            '5',
            ''
        )
        self.assertFalse(form.is_valid())
        self.assertIsNotNone(form.errors.as_data()['price'])

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
        self.assertIsNotNone(form.errors.as_data()['price'])

    def test_null_image(self):
        form_data = {'name': "Verre", 'amount': "2", 'price': "2.99"}
        form = GlassCreateForm(
            data=form_data,
            files={'image': None}
        )
        self.assertFalse(form.is_valid())
        self.assertIsNotNone(form.errors.as_data()['image'])