from django.views.generic import UpdateView
from django.urls import reverse_lazy

from glasses.models import Material
from glasses.forms.MaterialModelForm import MaterialModelForm

class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialModelForm
    template_name = "glasses/material_update.html"
    context_object_name = 'material'
    success_url = reverse_lazy('material_list')