from django.shortcuts import redirect


def update_cover_image(request):
    return redirect('dashboard_draft', request.user.username)
