from django.shortcuts import render
from users.forms import UserForms


def login(request):
    context = {'url': 'login'}
    return render(request, 'login.html', context)


def logout(request):
    context = {'url': 'logout'}
    return render(request, 'logout.html', context)


def signup(request):
    user_forms = UserForms
    context = {'url': 'signup', 'user_forms': user_forms}
    return render(request, 'signup.html', context)
