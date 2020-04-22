from django.shortcuts import redirect
from django.contrib.auth.models import User

def is_anonymous(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_anonymous:
            return function(request, *args, **kwargs)

        else:
            return redirect('account:login_page')

    return wrap

def user_must_have_profile(function):
    def wrap(request, *args, **kwargs):
        if request.user.email:
            users = User.objects.filter(
                email=request.user.email,
                social_auth__isnull=True,
                is_staff=False,
                is_superuser=False,
                username__icontains=request.user.username
            )
            users.delete()

        if hasattr(request.user, 'profile'):
            return function(request, *args, **kwargs)

        else:
            return redirect('account:profile_page')

    return wrap
