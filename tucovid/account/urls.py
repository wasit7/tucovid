from django.urls import path
from account.views import (
    login_page,
    profile_page,
    logout_view,
    profile_page_by_id
)

app_name = 'account'

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('profile/', profile_page, name='profile_page'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', profile_page_by_id, name='profile_page_by_id'),
]
