from django.shortcuts import render


def login(request):
    context = {'url': 'login'}
    return render(request, 'login.html', context)


def logout(request):
    context = {'url': 'logout'}
    return render(request, 'logout.html', context)


def signup(request):
    context = {'url': 'signup'}
    return render(request, 'signup.html', context)
