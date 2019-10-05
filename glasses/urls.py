from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /glasses/
    path('', views.index, name='index'),
    # ex: /glasses/5
    path('<int:glass_id>/', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )