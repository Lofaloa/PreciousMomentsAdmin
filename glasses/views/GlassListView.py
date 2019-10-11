from django.views.generic import ListView
from glasses.models import Glass

class GlassListView(ListView):
    model = Glass
    context_object_name = 'glasses'