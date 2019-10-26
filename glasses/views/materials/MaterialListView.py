from django.views.generic import ListView
from glasses.models import Material

class MaterialListView(ListView):
    model = Material
    context_object_name = 'materials'