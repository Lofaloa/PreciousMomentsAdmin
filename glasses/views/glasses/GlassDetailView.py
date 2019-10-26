from django.views.generic import DetailView
from glasses.models import Glass

class GlassDetailView(DetailView):
    model = Glass
    context_object_name = 'glass'