from django.urls import path
from account.views import login_page, profile_page, logout_view
from account.api_views import search_profile_api

app_name = 'account'

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('profile/', profile_page, name='profile_page'),
    path('logout/', logout_view, name='logout'),
    path('search/', search_profile_api, name='search_profile_api'),
]
