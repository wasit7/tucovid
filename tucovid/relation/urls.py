from django.urls import path
from relation.views import index, relation_page
from relation.api_views import relation_history

app_name = 'relation'

urlpatterns = [
    path('', index, name='index'),
    path('relation/', relation_page, name='relation_page'),
    path('relation/history/<int:user_id>/', relation_history, name='relation_history'),
]
