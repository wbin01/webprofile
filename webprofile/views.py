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


def login(request):
    context = {}
    return render(request, 'login.html', context)


def logout(request):
    context = {}
    return render(request, 'logout.html', context)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)
