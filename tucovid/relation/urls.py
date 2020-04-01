from django.urls import path
from relation.views import index, relation_page, event_page

app_name = 'relation'

urlpatterns = [
    path('', index, name='index'),
    path('relation/', relation_page, name='relation_page'),
    path('event/', event_page, name='event_page'),
]
