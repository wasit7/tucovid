from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.contrib.auth import logout, login
from django.conf import settings

TU_PROVIDER = 'tu'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')
    full_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=10)
    extra_attribute = JSONField(default=dict)

    def __str__(self):
        return self.full_name

def copy_user_data_to_exist_user(user, data):
    user.first_name = data.first_name
    user.last_name = data.last_name
    user.email = data.email
    user.is_active = True
    user.save()

    return user

def logged_in_handle(sender, user, request, **kwargs):
    social_auth = user.social_auth.all()

    if not social_auth.exists():
        return

    social_auth = social_auth.first()

    if social_auth.provider != TU_PROVIDER \
        or social_auth.uid == user.username:
        return

    existing_user = User.objects.get(username=social_auth.uid)

    if existing_user.is_superuser:
        return

    existing_user = copy_user_data_to_exist_user(existing_user, user)

    social_auth.user = existing_user
    social_auth.save()

    logout(request)
    login(request, existing_user, backend=settings.AUTHENTICATION_BACKENDS[0])

user_logged_in.connect(logged_in_handle)
