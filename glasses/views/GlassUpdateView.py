from django.views.generic import UpdateView
from django.urls import reverse_lazy

from glasses.models import Glass
from glasses.forms.glass_update_form import GlassUpdateForm

class GlassUpdateView(UpdateView):
    model = Glass
    form_class = GlassUpdateForm
    template_name = "glasses/glass_update.html"
    context_object_name = 'glass'
    success_url = reverse_lazy('glass_list')