from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from webprofile.forms import PostForms
from webprofile.models import Post


def index(request):

    posts = separate_posts_into_quantity_groups(
        posts_list=Post.objects.order_by(  # type: ignore
            '-publication_date').filter(post_is_published=True),
        items_quantity=3)

    # posts = (
    #     Post.objects  # type: ignore
    #     .order_by('-publication_date').filter(post_is_published=True))

    # paginator = Paginator(receitas, 6)
    # page = request.GET.get('page')
    # receitas_por_pagina = paginator.get_page(page)

    print('>>>>>>>>>>>', type(posts), posts)

    context = {'url': 'index', 'posts': posts}
    return render(request, 'index.html', context)


def content(request):
    context = {'url': 'content'}
    return render(request, 'content.html', context)


def create(request):
    post_forms = PostForms
    context = {
        'url': 'create',
        'post_forms': post_forms,
        'message_err': None}

    if request.method == 'POST':
        # name: request.user.first_name
        # username: request.user.username
        # username: auth.get_user(request)
        # email: request.user.email
        # password: request.user.password

        # request.FILES['image'] if 'image' in request.FILES else 'default.png'

        post = Post.objects.create(  # type: ignore
            user=get_object_or_404(User, pk=request.user.id),
            title=request.POST['title'],
            image=request.FILES.get('image', 'images/default.png'),
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


def edit(request, post_id):
    context = {'url': 'edit'}
    return render(request, 'edit.html')


def delete(request, post_id):
    return redirect('index')


def separate_posts_into_quantity_groups(
        posts_list: list, items_quantity: int) -> list:
    """Separate on groups

    if quantity groups is 3...
    move this:
    [obj, obj, obj, obj, obj, obj]

    for this:
    [[obj, obj, obj], [obj, obj, obj]]

    :param posts_list:
    :param items_quantity:
    :return:
    """

    all_post_groups_list = []
    one_post_group_list = []
    for item in enumerate(posts_list):
        index_post, object_post = (item[0], item[1])

        if index_post != 0 and index_post % items_quantity == 0:
            all_post_groups_list.append(one_post_group_list)
            one_post_group_list = []

        one_post_group_list.append(object_post)
    all_post_groups_list.append(one_post_group_list)

    return all_post_groups_list
