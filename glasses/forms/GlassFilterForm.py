from django import forms
from glasses.models import Glass

class GlassFilterForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    