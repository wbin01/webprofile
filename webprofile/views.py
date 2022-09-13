from django.shortcuts import render
from webprofile.forms import PostForms
from django.contrib import auth


def index(request):
    context = {'url': 'index'}
    return render(request, 'index.html', context)


def content(request):
    context = {'url': 'content'}
    return render(request, 'content.html', context)


def create(request):
    post_forms = PostForms
    context = {
        'url': 'login',
        'post_forms': post_forms,
        'message_err': None}

    return render(request, 'create.html', context)
