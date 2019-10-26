from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from glasses.views.IndexView import IndexView
from glasses.views.glasses.GlassListView import GlassListView
from glasses.views.glasses.GlassDetailView import GlassDetailView
from glasses.views.glasses.GlassCreateView import GlassCreateView
from glasses.views.glasses.GlassDeleteView import GlassDeleteView
from glasses.views.glasses.GlassUpdateView import GlassUpdateView

urlpatterns = [
    # example: /
    path('', IndexView.as_view(), name="index"),
    # example: glasses/
    path('glasses/', GlassListView.as_view(), name="glass_list"),
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