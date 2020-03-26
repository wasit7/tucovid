from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

@require_GET
def index(request):
    if request.user.is_anonymous:
        return redirect('account:login_page')

    if not hasattr(request.user, 'profile'):
        return redirect('account:profile_page')
    
    return redirect('main_page')
