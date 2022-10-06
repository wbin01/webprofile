import json
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from webprofile.forms import PostForms
from webprofile.models import Post
from profiles.models import Profile

import views_validations


def index(request):
    # All posts of all users
    posts = views_validations.separate_posts_into_quantity_groups(
        posts_list=(
            Post.objects.order_by(  # type: ignore
                '-publication_date').filter(is_published=True)),
        items_quantity=2)

    carousel_posts = (
        [posts[0][0], posts[0][1], posts[1][0]]
        if posts and len(posts) >= 2 else [])

    # Posts per page
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_per_page = paginator.get_page(page)

    # Context
    context = {
        'url_context': 'index',
        'posts_per_page': posts_per_page,
        'carousel_posts': carousel_posts}

    # Add Profile to context
    if request.user.is_authenticated:
        try:
            user_profile = get_object_or_404(Profile, user=request.user.id)
        except Exception as err:
            print(err)
            user_profile = None

        context['user_profile'] = user_profile

    return render(request, 'index.html', context)


def search_post(request):
    posts = Post.objects.order_by(  # type: ignore
        '-publication_date').filter(is_published=True).filter(
        title__icontains=request.GET['q'])

    # Context
    context = {
        'url_context': 'search_post',
        'search_text': request.GET['q'],
        'posts': posts}

    # Add Profile to context
    if request.user.is_authenticated:
        try:
            user_profile = get_object_or_404(Profile, user=request.user.id)
        except Exception as err:
            print(err)
            user_profile = None

        context['user_profile'] = user_profile

    return render(request, 'search_post.html', context)


def search_tag(request):
    posts = Post.objects.order_by(  # type: ignore
        '-publication_date').filter(is_published=True).filter(
        category__icontains=request.GET['q'])

    # Context
    context = {
        'url_context': 'search_tag',
        'search_text': request.GET['q'],
        'posts': posts}

    # Add Profile to context
    if request.user.is_authenticated:
        try:
            user_profile = get_object_or_404(Profile, user=request.user.id)
        except Exception as err:
            print(err)
            user_profile = None

        context['user_profile'] = user_profile

    return render(request, 'search_tag.html', context)


def search_user(request):
    posts = Profile.objects.filter(  # type: ignore
        user__username__icontains=request.GET['q'])

    # Context
    context = {
        'url_context': 'search_user',
        'search_text': request.GET['q'],
        'posts': posts}

    # Add Profile to context
    if request.user.is_authenticated:
        try:
            user_profile = get_object_or_404(Profile, user=request.user.id)
        except Exception as err:
            print(err)
            user_profile = None

        context['user_profile'] = user_profile

    return render(request, 'search_user.html', context)


def content(request, url_title, post_id):
    print(url_title)

    # Post content
    post = Post.objects.get(pk=post_id)  # type: ignore

    # Tags
    post_tags = [x for x in post.category.split(',') if x.strip() != '']

    # Recomends
    recommended_posts = []
    for p in Post.objects.order_by(  # type: ignore
            '-publication_date').filter(is_published=True):
        for tag in post_tags:
            if tag in p.category:
                recommended_posts.append(p)
                break
        if len(recommended_posts) >= 5:
            break

    # Access (hidden content only for post.user.id)
    if request.user.id != post.user.id and not post.is_published:
        return redirect('index')

    # Profile
    try:
        user_profile = get_object_or_404(Profile, user=request.user.id)
    except Exception as err:
        print(err)
        user_profile = None

    context = {
        'url_context': 'content',
        'post': post,
        'recommended_posts': recommended_posts,
        'post_tags': post_tags,
        'user_profile': user_profile}

    return render(request, 'content.html', context)


def create(request, url_to_go_back):
    # Access
    if not request.user.is_authenticated:
        return redirect('index')

    # Profile
    try:
        user_profile = get_object_or_404(Profile, user=request.user.id)
    except Exception as err:
        print(err)
        user_profile = None

    # Post forms
    post_forms = PostForms

    # Context
    context = {
        'url_context': 'create',
        'url_to_go_back': url_to_go_back,
        'post_forms': post_forms,
        'message_err': None,
        'user_profile': user_profile}

    # Work on sent request
    if request.method == 'POST':
        # username: auth.get_user(request)
        post_content = request.POST['content']
        content_text = json.loads(post_content)['html'] if post_content else ''

        # Create post with sent request
        post = Post.objects.create(  # type: ignore
            # user=get_object_or_404(User, pk=request.user.id),
            user=request.user,
            title=request.POST['title'],
            url_title=views_validations.normalize_title(request.POST['title']),
            image=request.FILES.get('image', 'post-default.svg'),
            summary=request.POST['summary'],
            content=content_text,
            category=request.POST['category'].lower().strip(),
            publication_date=timezone.now(),
            is_published=True if 'is_published' in request.POST else False,
            is_for_main_page=(
                True if 'is_for_main_page' in request.POST else False)
        )

        # Save post
        post.save()

        # Go to url
        if 'is_published' not in request.POST:
            return redirect('dashboard_draft', request.user.username)

        if url_to_go_back == 'index':
            return redirect('index')

        return redirect('dashboard', request.user.username)

    return render(request, 'create.html', context)


def edit(request, url_title, post_id, url_to_go_back):
    # Post
    post_to_edit = get_object_or_404(Post, pk=post_id)

    # Access
    if (request.user.id == post_to_edit.user.id or
            request.user.is_superuser):
        # Form
        post_forms = PostForms(
            initial={
                'user': post_to_edit.user.id,
                'title': post_to_edit.title,
                'url_title': post_to_edit.url_title,
                'image': post_to_edit.image.url,
                'summary': post_to_edit.summary,
                'content': post_to_edit.content,
                'category': post_to_edit.category,
                'publication_date': timezone.now(),
                'is_published': post_to_edit.is_published,
                'is_for_main_page': post_to_edit.is_for_main_page,
            })

        # Image Label with old image name
        post_forms['image'].label = (
                    '<h5>Imagem</h5>'
                    '<small class="text-muted">Capa do card</small></br>'
                    '<small class="text-primary text-opacity-50"> ' +
                    str(post_to_edit.image.url.split("/")[-1]) +
                    '</small>')

        # Profile
        try:
            user_profile = get_object_or_404(Profile, user=request.user.id)
        except Exception as err:
            print(err)
            user_profile = None

        # Context
        context = {
            'url_context': 'edit',
            'url_to_go_back': url_to_go_back,
            'post_forms': post_forms,
            'post_id': post_id,
            'post_user_id': post_to_edit.user.id,
            'post_user_first_name': post_to_edit.user.first_name,
            'post_title': post_to_edit.title,
            'url_title': url_title,

            'message_err': None,
            'user_profile': user_profile}

        return render(request, 'edit.html', context)

    return redirect('index')


def update(request, post_id):
    if request.method == 'POST':

        # Post
        post = Post.objects.get(pk=post_id)  # type: ignore

        # Access
        if (request.user.id == post.user.id or
                request.user.is_superuser):

            post_content = request.POST['content']
            content_text = json.loads(post_content)['html'] if post_content else ''

            # Update post
            url_title = views_validations.normalize_title(request.POST['title'])

            post.title = request.POST['title']
            post.url_title = url_title
            post.summary = request.POST['summary']
            post.content = content_text
            post.category = request.POST['category']
            post.publication_date = timezone.now()
            post.is_published = True if 'is_published' in request.POST else False
            post.is_for_main_page = (
                True if 'is_for_main_page' in request.POST else False)
            if 'image' in request.FILES:
                post.image = request.FILES['image']

            # Save updated post
            post.save()

            # Go to url
            return redirect('content', url_title, post_id)

    return redirect('index')


def delete(request, url_to_go_back, post_id):
    # Post
    post = get_object_or_404(Post, pk=post_id)

    # Access
    if (request.user.id == post.user.id or
            request.user.is_superuser):
        # Delete
        post.delete()

        # Go to url
        if 'dashboard' in url_to_go_back:
            return redirect(url_to_go_back, request.user.username)

    return redirect('index')
