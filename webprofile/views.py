from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from webprofile.forms import PostForms
from webprofile.models import Post

import views_validations


def index(request):
    # All posts of all users
    posts = views_validations.separate_posts_into_quantity_groups(
        posts_list=Post.objects.order_by(  # type: ignore
            '-publication_date').filter(is_published=True),
        items_quantity=2)

    # Posts per page
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_per_page = paginator.get_page(page)

    # Context
    context = {
        'url': 'index',
        'posts_per_page': posts_per_page}

    return render(request, 'index.html', context)


def content(request, post_id):
    post = Post.objects.get(pk=post_id)  # type: ignore
    context = {'url': 'content', 'post': post}
    return render(request, 'content.html', context)


def create(request):
    # Access
    if not request.user.is_authenticated:
        return redirect('index')

    # Post forms
    post_forms = PostForms

    # Context
    context = {
        'url': 'create',
        'post_forms': post_forms,
        'message_err': None}

    # Work on sent request
    if request.method == 'POST':
        # name: request.user.first_name
        # username: request.user.username
        # username: auth.get_user(request)
        # email: request.user.email
        # password: request.user.password

        # Create post with sent request
        post = Post.objects.create(  # type: ignore
            user=get_object_or_404(User, pk=request.user.id),
            title=request.POST['title'],
            image=request.FILES.get('image', 'images/default.png'),
            summary=request.POST['summary'],
            content=views_validations.content_as_p(request.POST['content']),
            category=request.POST['category'].lower(),
            publication_date=timezone.now(),
            is_published=(
                False if request.POST['is_published'] == 'no' else True)
        )

        # Save post
        post.save()

        # Go to url
        return redirect('index')

    return render(request, 'create.html', context)


def edit(request, post_id):
    # Access
    if not request.user.is_authenticated:
        return redirect('index')

    # Post
    post_to_edit = get_object_or_404(Post, pk=post_id)

    # Form
    post_forms = PostForms(
        initial={
            'user': get_object_or_404(User, pk=request.user.id),
            'title': post_to_edit.title,
            'image': post_to_edit.image.url,
            'summary': post_to_edit.summary,
            'content': views_validations.content_rm_p(post_to_edit.content),
            'category': post_to_edit.category,
            'publication_date': timezone.now(),
            'is_published': (
                ('no', 'Não') if not post_to_edit.is_published
                else ('yes', 'Sim'))
        })

    # Context
    context = {
        'url': 'edit',
        'post_forms': post_forms,
        'post_id': post_id,
        'message_err': None}

    return render(request, 'edit.html', context)


def update(request, post_id):
    # Access
    if not request.user.is_authenticated:
        return redirect('index')

    # Work on sent request
    if request.method == 'POST':

        # Get post
        post = Post.objects.get(pk=post_id)  # type: ignore

        # Update post
        post.title = request.POST['title']
        post.summary = request.POST['summary']
        post.content = views_validations.content_as_p(request.POST['content'])
        post.category = request.POST['category']
        post.publication_date = timezone.now()
        post.is_published = (
                False if request.POST['is_published'] == 'no' else True)
        if 'image' in request.FILES:
            post.image = request.FILES['image']

        # Save updated post
        post.save()

        # Go to url
        return redirect('content', post_id)


def delete(request, post_id):
    # Access
    if not request.user.is_authenticated:
        return redirect('index')

    # Post
    post = get_object_or_404(Post, pk=post_id)

    # Delete
    post.delete()

    return redirect('index')
