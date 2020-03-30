from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods
from relation.relation import create_relation_record, create_event_record
from relation.models import RELATION_LEVELS
from account.decorators import user_must_have_profile
import json

@require_GET
@login_required
@user_must_have_profile
def index(request):
    return redirect('relation:relation_page')

@require_http_methods(['GET', 'POST'])
@login_required
@user_must_have_profile
def relation_page(request):
    if request.method == 'GET':
        context = dict()
        context['relation_level'] = RELATION_LEVELS
        
        return render(request, 'relation/relation.html', context=context)

    elif request.method == 'POST':
        body = request.body
        body = json.loads(body)
        relation = create_relation_record(request.user, body)

        return JsonResponse(data=relation, status=200)

@require_http_methods(['GET', 'POST'])
@login_required
@user_must_have_profile
def event_page(request):
    if request.method == 'GET':
        return render(request, 'relation/event.html')

    elif request.method == 'POST':
        body = request.body
        body = json.loads(body)
        event = create_event_record(request.user, body)

        return JsonResponse(data=event, status=200)
