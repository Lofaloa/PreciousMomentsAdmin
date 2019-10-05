from django.http import HttpResponse
from django.shortcuts import render

from .models import Glass

def index(request):
    glasses = Glass.objects.all()
    return render(request, 'glasses/index.html', {'glasses': glasses})

def detail(request, glass_id):
    glass = Glass.objects.get(pk=glass_id)
    return render(request, 'glasses/detail.html', {'glass': glass})