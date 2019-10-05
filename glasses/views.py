from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Glass

def index(request):
    glasses = Glass.objects.all()
    return render(request, 'glasses/index.html', {'glasses': glasses})

def detail(request, glass_id):
    glass = get_object_or_404(Glass, pk=glass_id)
    return render(request, 'glasses/detail.html', {'glass': glass})