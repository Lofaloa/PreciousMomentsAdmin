from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Glass
from .forms import GlassModelForm

def index(request):
    glasses = Glass.objects.all()
    form = GlassModelForm()
    return render(request, 'glasses/index.html', {
        'glasses': glasses,
        'glass_form' : form
    })

def detail(request, glass_id):
    glass = get_object_or_404(Glass, pk=glass_id)
    return render(request, 'glasses/detail.html', {'glass': glass})

def get_glass(request):
    glass = None
    if request.method == 'POST':
        form = GlassModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('index')