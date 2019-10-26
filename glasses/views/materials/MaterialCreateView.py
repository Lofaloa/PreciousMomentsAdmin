from django.views.generic import CreateView
from django.urls import reverse_lazy

from glasses.models import Material
from glasses.forms.MaterialModelForm import MaterialModelForm

class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialModelForm
    template_name = "glasses/material_create.html"
    context_object_name = 'materials'
    success_url = reverse_lazy('material_list')