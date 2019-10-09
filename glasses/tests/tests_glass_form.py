from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.conf import settings
from glasses.forms import GlassModelForm

from unittest.mock import MagicMock
from django.core.files import File

from glasses.tests.test_image import TEST_IMAGE

import os

class GlassModelFormTests(TestCase):

    def create_glass_form(self, name, amount, price):
        """
        Creates a form with the specified data and a test image.
        """
        form_data = {
            'name': name,
            'amount': amount,
            'price': price
        }
        return GlassModelForm(data=form_data, files={'image': MagicMock(spec=File, name='image')})

    def test_valid_data(self):
        form = self.create_glass_form('Verre à tournesol', '5', '4.99')
        print(form.errors.as_data())
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