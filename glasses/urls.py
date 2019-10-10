from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /glasses/
    path('', views.index, name='index'),
    # ex: /glasses/5
    path('<int:glass_id>/', views.detail, name='detail'),
    #ex: /glasses/add
    path('add/', views.add, name='add'),
    #ex: /glasses/5/delete
    path('<int:glass_id>/delete', views.delete, name='delete'),
    #ex: /glasses/5/edit
    path('<int:glass_id>/edit', views.edit, name='edit')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )