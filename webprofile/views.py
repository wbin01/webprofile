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

    if request.method == 'POST':
        get_title = request.POST['title']
        get_image = request.POST['image']
        get_summary = request.POST['summary']
        get_content = request.POST['content']
        get_category = request.POST['category']
        get_publication_date = request.POST['publication_date']
        get_post_is_published = request.POST['post_is_published']

        # name: request.user.first_name
        # username: request.user.username
        # username 2: auth.get_user(request)
        # email: request.user.email
        # password: request.user.password

        print('title:', get_title)
        print('image:', get_image)
        print('summary:', get_summary)
        print('content:', get_content)
        print('category:', get_category)
        print('publication_date:', get_publication_date)
        print('post_is_published:', get_post_is_published)

        # post = PostForms()

    return render(request, 'create.html', context)
