from django.shortcuts import render
from .github import repositories

def projects(request):
    repos = repositories()
    return render(request, 'projects/projects.html', {'repos': repos})