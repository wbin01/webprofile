from django.shortcuts import redirect


def update_cover_image(request):
    return redirect('dashboard', request.user.username)


def update_profile_image(request):
    return redirect('dashboard', request.user.username)
