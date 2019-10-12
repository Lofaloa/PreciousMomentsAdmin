from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from glasses.models import Glass

class GlassModelForm(forms.ModelForm):

    class Meta:
        model = Glass
        fields = ('name', 'category', 'amount', 'price', 'image')
        labels = {
            "name": "Nom personnalisé",
            "category": "Catégorie",
            "amount": "Nombre de paires disponibles",
            "price": "Prix de vente",
            "image": "Photo du verre",
        }
        help_texts = {
            'name': 'Choisissez un nom unique qui correspond à votre réalisation',
            "category": "Ce champ correspond au type de votre réalisation",
            'amount': 'Le nombre de paire doit être positif',
            'price': 'Le prix doit être positif',
            'image': 'Choisissez une photo qui représente votre réalisation',
        }