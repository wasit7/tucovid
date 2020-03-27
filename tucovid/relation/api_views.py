from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from relation.relation import get_history_relation, get_event_history

@require_GET
@login_required
def relation_history(request, user_id):
    relation_history = get_history_relation(user_id)

    return JsonResponse(data=relation_history, status=200, safe=False)

@require_GET
@login_required
def event_history(request, user_id):
    event_history = get_event_history(user_id)

    return JsonResponse(data=relation_history, status=200, safe=False)
