from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def content(request):
    context = {}
    return render(request, 'content.html', context)


def create(request):
    context = {}
    return render(request, 'create.html', context)
