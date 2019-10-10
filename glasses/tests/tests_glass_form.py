from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.test import TestCase, override_settings
from django.conf import settings

from glasses.forms import GlassModelForm
from glasses.tests.test_image import TEST_IMAGE

from unittest.mock import MagicMock

import os

class GlassModelFormTests(TestCase):

    def create_glass_form(self, name, amount, price):
        form_data = {'name': name, 'amount': amount, 'price': price}
        return GlassModelForm(
            data=form_data, 
            files={'image': MagicMock(spec=File, name="image")}
        )

    def test_null_glass_name(self):
        """
        The form should not be valid when the glass name is null (None).
        """
        form = self.create_glass_form(
            None,
            '5',
            '4.99'
        )
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
        self.assertIsNotNone(form.errors.as_data()['name'])

    def test_null_amount(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            None,
            '4.99'
        )
        self.assertIsNotNone(form.errors.as_data()['amount'])

    def test_blank_amount(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            '',
            '4.99'
        )
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
        self.assertIsNotNone(form.errors.as_data()['amount'])

    def test_null_price(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            '5',
            None
        )
        self.assertIsNotNone(form.errors.as_data()['price'])

    def test_blank_price(self):
        form = self.create_glass_form(
            'Verre à tournesol',
            '5',
            ''
        )
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
        self.assertIsNotNone(form.errors.as_data()['price'])