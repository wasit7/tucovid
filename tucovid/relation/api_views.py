from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from relation.relation import get_history_relation

@require_GET
@login_required
def relation_history(request, user_id):
    relation_history = get_history_relation(user_id)

    return JsonResponse(data=relation_history, status=200, safe=False)
