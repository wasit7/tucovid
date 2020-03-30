from django.urls import path
from account.views import (
    login_page,
    profile_page,
    logout_view,
    profile_page_by_id
)
from account.api_views import (
    search_relation_profile_api,
    search_profile_api
)

app_name = 'account'

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('profile/', profile_page, name='profile_page'),
    path('logout/', logout_view, name='logout'),
    path('relation/search/', search_relation_profile_api, name='search_relation_profile_api'),
    path('event/search/', search_profile_api, name='search_profile_api'),
    path('profile/<int:user_id>/', profile_page_by_id, name='profile_page_by_id'),
]
