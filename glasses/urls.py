from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from glasses.views.IndexView import IndexView
from glasses.views.glasses.GlassListView import GlassListView
from glasses.views.glasses.GlassDetailView import GlassDetailView
from glasses.views.glasses.GlassCreateView import GlassCreateView
from glasses.views.glasses.GlassDeleteView import GlassDeleteView
from glasses.views.glasses.GlassUpdateView import GlassUpdateView

from glasses.views.materials.MaterialListView import MaterialListView
from glasses.views.materials.MaterialCreateView import MaterialCreateView
from glasses.views.materials.MaterialDeleteView import MaterialDeleteView
from glasses.views.materials.MaterialUpdateView import MaterialUpdateView

urlpatterns = [

    # example: /
    path('', IndexView.as_view(), name="index"),

    # example: glasses/
    path('glasses/', GlassListView.as_view(), name="glass_list"),
    # example: glasses/5
    path('glasses/<int:pk>/', GlassDetailView.as_view(), name="glass_detail"),
    # example: glasses/create
    path('glasses/create/', GlassCreateView.as_view(), name="glass_create"),
    # example: glasses/5/delete
    path('glasses/<int:pk>/delete', GlassDeleteView.as_view(), name="glass_delete"),
    # example: glasses/5/update
    path('glasses/<int:pk>/update', GlassUpdateView.as_view(), name="glass_update"),

    # example: materials/
    path('materials/', MaterialListView.as_view(), name="material_list"),
    # example: materials/create
    path('materials/create/', MaterialCreateView.as_view(), name="material_create"),
    # example: glasses/5/delete
    path('materials/<int:pk>/delete', MaterialDeleteView.as_view(), name="material_delete"),
    # example: materials/5/update
    path('materials/<int:pk>/update', MaterialUpdateView.as_view(), name="material_update"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )