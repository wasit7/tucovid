from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods
from account.decorators import is_anonymous
from account.profile import get_profile_if_exists, update_or_create_profile

@require_GET
@is_anonymous
def login_page(request):
    return render(request, 'account/login.html')

@require_http_methods(['GET', 'POST'])
@login_required
def profile_page(request):
    context = dict()

    if request.method == 'GET':
        context['profile'] = profile = get_profile_if_exists(request.user)

        return render(request, 'account/profile.html', context=context)

    elif request.method == 'POST':
        profile, is_created = update_or_create_profile(request.user, request.POST)

        if is_created:
            return redirect('index page') # index page

        else:
            context['profile'] = profile
            return render(request, 'account/profile.html', context=context)
