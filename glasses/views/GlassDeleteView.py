from django.views.generic import DeleteView
from django.urls import reverse_lazy

from glasses.models import Glass

class GlassDeleteView(DeleteView):
    model = Glass
    template_name = "glasses/glass_delete.html"
    context_object_name = 'glass'
    success_url = reverse_lazy('glass_list')