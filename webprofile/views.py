from django.shortcuts import render


def index(request):
    context = {'url': 'index'}
    return render(request, 'index.html', context)


def content(request):
    context = {'url': 'content'}
    return render(request, 'content.html', context)


def create(request):
    context = {'url': 'create'}
    return render(request, 'create.html', context)
