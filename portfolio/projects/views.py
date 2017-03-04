from django.shortcuts import render


def projects(request):
    return render(request, 'projects/base.html', {})