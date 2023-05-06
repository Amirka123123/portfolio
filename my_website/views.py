from django.shortcuts import render

from my_website.models import Project


def index(request):
    return render(request, 'projects.html')


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project_detail.html', context)


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)
