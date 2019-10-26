from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from glasses.models import Material

class MaterialModelForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('name', 'available_amount', 'price', 'supplier')
        labels = {
            "name": "Nom",
            "available_amount": "Quantité disponible",
            "price": "Prix d'achat",
            "supplier": "Fournisseur",
        }
        help_texts = {
            "name": "Choisissez un nom clair qui représente le matériel",
            "available_amount": "Quantité d'unités disponibles dans votre atelier",
            "price": "Prix auquel vous avez acheté ce matériel",
        }