from django.shortcuts import redirect

def is_anonymous(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_anonymous:
            return function(request, *args, **kwargs)

        else:
            return redirect('account:login_page')

    return wrap

def user_must_have_profile(function):
    def wrap(request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            return function(request, *args, **kwargs)

        else:
            return redirect('account:profile_page')

    return wrap
