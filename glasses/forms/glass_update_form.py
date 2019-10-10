from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from glasses.models import Glass

class GlassUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['amount'].required = False
        self.fields['price'].required = False
        self.fields['image'].required = False

    class Meta:
        model = Glass
        fields = ('name', 'amount', 'price', 'image')
        labels = {
            "name": "Nom personnalisé",
            "amount": "Nombre de verres disponibles",
            "price": "Prix de vente",
            "image": "Photo du verre",
        }
        help_texts = {
            'name': 'Choisissez un nom unique qui correspond à votre réalisation',
            'amount': 'La quantié doit être positive',
            'price': 'Le prix doit être positif',
            'image': 'Choisissez une photo qui représente votre réalisation',
        }