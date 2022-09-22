from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from profiles.models import Profile


def update_cover_image(request):
    if request.method == 'POST':
        # Get profile
        if create_profile_if_not_exist(request):
            profile = get_object_or_404(Profile, user=request.user.id)

            # Update image
            if 'cover_image' in request.FILES:
                profile.cover_image = request.FILES['cover_image']
                profile.save()

    return redirect('dashboard', request.user.username)


def update_profile_image(request):
    return redirect('dashboard', request.user.username)


def create_profile_if_not_exist(request) -> bool:
    try:
        get_object_or_404(Profile, user=request.user.id)
    except Exception as err:
        print(f'>>> Profile DoesNotExist! "Exception" error is: "{err}"')
    else:
        print(f'>>> Profile for user "{request.user.username}" found!')
        return True

    print('>>> Creating profile...')
    try:
        profile = Profile.objects.create(  # type: ignore
            user=get_object_or_404(User, pk=request.user.id),
            profile_image=request.FILES.get(
                'profile_image', 'images/cover-default.png'),
            cover_image=request.FILES.get(
                'cover_image', 'images/profile-default.png'),
        )
        profile.save()
    except Exception as err:
        print(f'>>> Profile cannot be created: "{err}"')
        return False
    else:
        print(f'>>> Profile for "{request.user.username}" has been created!')
        return True
