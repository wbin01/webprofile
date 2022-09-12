from django.shortcuts import render


def login(request):
    context = {}
    return render(request, 'login.html', context)


def logout(request):
    context = {}
    return render(request, 'logout.html', context)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)
