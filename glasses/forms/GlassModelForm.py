from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from glasses.models import Glass
from glasses.models import Material

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
    
    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        label="Matériels",
        help_text="Sélectionnez les éléments dans la liste."
    )

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):               
            initial = kwargs.setdefault('initial', {})
            initial['materials'] = [material.pk for material in kwargs['instance'].material_set.all()]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)
        old_save_m2m = self.save_m2m
        
        def save_m2m():
           old_save_m2m()
           instance.material_set.clear()
           instance.material_set.add(*self.cleaned_data['materials'])
        self.save_m2m = save_m2m

        if commit:
            instance.save()
            self.save_m2m()

        return instance