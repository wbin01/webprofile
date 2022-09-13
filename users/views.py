from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from users.forms import SignUpForms, LoginForms
import string


def login(request):
    user_forms = LoginForms
    context = {
        'url': 'login',
        'user_forms': user_forms,
        'message_err': None}

    if request.method == 'POST':
        # Username
        username = request.POST['username']
        if not username.strip():
            context['message_err'] = 'Preencha o nome de usuário'

        # Password
        password = request.POST['password']
        if not password.strip():
            context['message_err'] = 'Preencha a senha'

        # User
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(
                request, username=username, password=password)

            # Auth
            if user is not None:
                auth.login(request, user)
                return redirect('index')

            # Errors
            if context['message_err']:
                return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def logout(request):
    context = {'url': 'logout'}
    return render(request, 'logout.html', context)


def signup(request):
    user_forms = SignUpForms
    context = {
        'url': 'signup',
        'user_forms': user_forms,
        'message_err': None}

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        valid_chars = list(string.ascii_letters + string.digits)

        # Name
        if not name.strip():
            context['message_err'] = 'Preencha o nome'
        elif len(name) >= 200:
            context['message_err'] = 'Nome muito longo'
        elif any(char not in valid_chars + [' '] for char in name):
            context['message_err'] = 'Nome nulo! Use letras, números e espaços'

        # Username
        elif not username.strip():
            context['message_err'] = 'Preencha o nome de usuário'
        elif not username.isalpha():
            context['message_err'] = 'Nome de usuário só pode conter letras'

        # Email
        elif not email.strip():
            context['message_err'] = 'Preencha o email'

        # Password
        elif not password.strip() or not password_confirm.strip():
            context['message_err'] = 'Preencha a senha'
        elif password != password_confirm:
            context['message_err'] = 'As senhas não correspondem'
        elif (len(password) < 8 or
              all(char.isalpha() for char in password) or
              all(char.isdigit() for char in password) or
              any(char not in valid_chars for char in password)):
            context['message_err'] = 'Senha inválida'

        # Exists
        if User.objects.filter(username=username).exists():
            context['message_err'] = 'Usuário já cadastrado'
        if User.objects.filter(email=email).exists():
            context['message_err'] = 'Email já cadastrado'

        # Errors
        if context['message_err']:
            return render(request, 'signup.html', context)

        # User
        user = User.objects.create_user(
            username=username, first_name=name, email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, 'signup.html', context)
