from django import forms
from .models import Glass

class GlassModelForm(forms.ModelForm):
    class Meta:
        model = Glass
        fields = ('name', 'amount', 'price', 'image')