from django.views.generic import DeleteView
from django.urls import reverse_lazy

from glasses.models import Material

class MaterialDeleteView(DeleteView):
    model = Material
    template_name = "glasses/material_delete.html"
    context_object_name = 'material'
    success_url = reverse_lazy('material_list')