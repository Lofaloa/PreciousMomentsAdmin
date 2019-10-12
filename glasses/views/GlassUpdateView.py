from django.views.generic import UpdateView
from django.urls import reverse_lazy

from glasses.models import Glass
from glasses.forms.GlassModelForm import GlassModelForm

class GlassUpdateView(UpdateView):
    model = Glass
    form_class = GlassModelForm
    template_name = "glasses/glass_update.html"
    context_object_name = 'glass'
    success_url = reverse_lazy('glass_list')