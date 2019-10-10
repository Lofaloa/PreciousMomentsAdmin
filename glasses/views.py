from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Glass
from glasses.forms.glass_update_form import GlassUpdateForm
from glasses.forms.glass_create_form import GlassCreateForm

def index(request):
    glasses = Glass.objects.all()
    if request.method == 'POST':
        form = GlassCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = GlassCreateForm()
    return render(request, 'glasses/index.html', {
        'glasses': glasses,
        'glass_form' : form
    })

def detail(request, glass_id):
    glass = get_object_or_404(Glass, pk=glass_id)
    return render(request, 'glasses/detail.html', {'glass': glass})

def add(request):
    if request.method == 'POST':
        form = GlassCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GlassCreateForm()
    return render(request, 'glasses/add.html', {'form': form})

def edit(request, glass_id):
    glass = get_object_or_404(Glass, pk=glass_id)
    if request.method == 'POST':
        form = GlassUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('detail', glass_id)
    else:
        form = GlassUpdateForm()
    return render(request, 'glasses/edit.html', {'form': form})

def delete(request, glass_id):
    glass = get_object_or_404(Glass, pk=glass_id)
    glass.delete()
    return redirect('index')