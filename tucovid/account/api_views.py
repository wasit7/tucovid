from django.http import JsonResponse
from account.profile import search_profile
from django.views.decorators.http import require_POST
from relation.models import Relationship
import json

@require_POST
def search_profile_api(request):
    body = request.body
    body = json.loads(body)
    keyword = body['keyword']
    reporter_id = int(body['reporter_id'])

    profiles = search_profile(keyword)
    response = []

    for profile in profiles.exclude(pk=reporter_id):
        if not Relationship.objects.filter(persons__pk=reporter_id).filter(persons__pk=profile.user.pk).exists():
            response.append({
                'id': profile.user.pk,
                'full_name': profile.full_name,
                'phone_no': profile.phone_no,
                'extra_attribute': profile.extra_attribute
            })

    return JsonResponse(data=response, status=200, safe=False)
