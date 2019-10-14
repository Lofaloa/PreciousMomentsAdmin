from django.views.generic import ListView
from glasses.models import Glass

class GlassListView(ListView):
    model = Glass
    context_object_name = 'glasses'

    def get_queryset(self):
        selection = self.request.GET.get('name')
        if selection:
            return Glass.objects.filter(name__contains=selection)
        else:
            return Glass.objects.all()