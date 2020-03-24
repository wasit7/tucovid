from django.urls import path
from account.views import login_page

app_name = 'account'

urlpatterns = [
    path('login', login_page, name='login_page')
]
