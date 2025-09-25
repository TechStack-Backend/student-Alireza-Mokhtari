from django.shortcuts import render, redirect, get_object_or_404
from .models import Developer, Project
from .forms import DeveloperForm, ProjectForm

def developers_list(request):
    devs = Developer.objects.all().prefetch_related('projects', 'skills')
    return render(request, 'core/developers_list.html', {'developers': devs})

def projects_list(request):
    projs = Project.objects.all().prefetch_related('developers')
    return render(request, 'core/projects_list.html', {'projects': projs})

def developer_create(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('developers_list')
    else:
        form = DeveloperForm()
    return render(request, 'core/developer_form.html', {'form': form})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            proj = form.save() 
            return redirect('projects_list')
    else:
        form = ProjectForm()
    return render(request, 'core/project_form.html', {'form': form})

def home(request):
    return render(request, 'core/home.html')