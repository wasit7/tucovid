from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods
from relation.relation import create_relation_record
from relation.models import RELATION_LEVELS
import json

@require_GET
def index(request):
    if request.user.is_anonymous:
        return redirect('account:login_page')

    if not hasattr(request.user, 'profile'):
        return redirect('account:profile_page')
    
    return redirect('relation:relation_page')

@require_http_methods(['GET', 'POST'])
@login_required
def relation_page(request):
    context = dict()

    if request.method == "GET":
        context['relation_level'] = RELATION_LEVELS
        
        return render(request, 'relation/relation.html', context=context)

    else:
        body = request.body
        body = json.loads(body)
        relation = create_relation_record(request.user, body)

        return JsonResponse(data=relation, status=200)
