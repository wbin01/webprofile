from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from webprofile.forms import PostForms
from webprofile.models import Post


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

    if request.method == 'POST':
        # name: request.user.first_name
        # username: request.user.username
        # username: auth.get_user(request)
        # email: request.user.email
        # password: request.user.password

        post = Post.objects.create(  # type: ignore
            user=get_object_or_404(User, pk=request.user.id),
            title=request.POST['title'],
            image=request.POST['image'],
            summary=request.POST['summary'],
            content=request.POST['content'],
            category=request.POST['category'].lower(),
            publication_date=timezone.now(),
            post_is_published=(
                False if request.POST['post_is_published'] == 'no' else True)
        )
        post.save()
        return redirect('index')

    return render(request, 'create.html', context)
