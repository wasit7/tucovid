from django.http import JsonResponse
from django.views.decorators.http import require_POST
from account.profile import search_profile
from account.datasources import map_profile
from relation.models import Relationship
import json

@require_POST
def search_relation_profile_api(request):
    body = request.body
    body = json.loads(body)
    keyword = body['keyword']

    profiles = search_profile(keyword)
    response = []

    reporter_id = None
    
    if body['reporter_id']:
        reporter_id = int(body['reporter_id'])
        profiles = profiles.exclude(user__pk=reporter_id)

    for profile in profiles:
        if not Relationship.objects.filter(persons__pk=reporter_id).filter(persons__pk=profile.user.pk).exists():
            response.append(map_profile(profile))

    return JsonResponse(data=response, status=200, safe=False)

@require_POST
def search_profile_api(request):
    body = request.body
    body = json.loads(body)
    keyword = body['keyword']

    profiles = search_profile(keyword)
    excluding_ids = []

    if body['excluding_ids']:
        excluding_ids = [ int(id) for id in body['excluding_ids'] ]

    response = [ map_profile(profile) for profile in profiles.exclude(user__pk__in=excluding_ids) ]

    return JsonResponse(data=response, status=200, safe=False)
