from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from glasses.views.GlassListView import GlassListView
from glasses.views.GlassDetailView import GlassDetailView
from glasses.views.GlassCreateView import GlassCreateView
from glasses.views.GlassDeleteView import GlassDeleteView
from glasses.views.GlassUpdateView import GlassUpdateView

urlpatterns = [
    # example: glasses/
    path('', GlassListView.as_view(), name="glass_list"),
    # example: glasses/5    
    path('<int:pk>/', GlassDetailView.as_view(), name="glass_detail"),
    # example: glasses/create    
    path('create/', GlassCreateView.as_view(), name="glass_create"),
    # example: glasses/5/delete    
    path('<int:pk>/delete', GlassDeleteView.as_view(), name="glass_delete"),
    # example: glasses/5/update    
    path('<int:pk>/update', GlassUpdateView.as_view(), name="glass_update"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )