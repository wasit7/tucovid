from django.shortcuts import render
from django.views.decorators.http import require_GET
from account.decorators import is_anonymous

@require_GET
@is_anonymous
def login_page(request):
    return render(request, 'account/login.html')
