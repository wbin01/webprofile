from django.shortcuts import render, redirect
from users.forms import UserForms
import string


def login(request):
    context = {'url': 'login'}
    return render(request, 'login.html', context)


def logout(request):
    context = {'url': 'logout'}
    return render(request, 'logout.html', context)


def signup(request):
    user_forms = UserForms
    context = {
        'url': 'signup',
        'user_forms': user_forms,
        'message_err': None}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        valid_password_chars = list(string.ascii_letters + string.digits)

        if not name.strip():
            context['message_err'] = 'Preencha o nome'
        elif not email.strip():
            context['message_err'] = 'Preencha o email'
        elif not password.strip() or not password_confirm.strip():
            context['message_err'] = 'Preencha a senha'
        elif password != password_confirm:
            context['message_err'] = 'As senhas não correspondem'
        elif (len(password) < 8 or
              all(char.isalpha() for char in password) or
              all(char.isdigit() for char in password) or
              any(char not in valid_password_chars for char in password)):
            context['message_err'] = 'Senha inválida'

        if context['message_err']:
            return render(request, 'signup.html', context)
        else:
            return redirect('login')

    return render(request, 'signup.html', context)
