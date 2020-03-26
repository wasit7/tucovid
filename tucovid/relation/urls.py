from django.urls import path
from relation.views import index

app_name = 'relation'

urlpatterns = [
    path('', index, name='index')
]
