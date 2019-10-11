from django.views.generic import CreateView
from django.urls import reverse_lazy

from glasses.models import Glass
from glasses.forms.glass_create_form import GlassCreateForm

class GlassCreateView(CreateView):
    model = Glass
    form_class = GlassCreateForm
    template_name = "glasses/glass_create.html"
    context_object_name = 'glasses'
    success_url = reverse_lazy('glass_list')