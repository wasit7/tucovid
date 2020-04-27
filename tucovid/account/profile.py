from django.contrib.auth.models import User
from django.db.models import Q
from account.models import Profile
from relation.models import Relationship

def get_user_by_id(user_id):
    return User.objects.get(id=user_id)

def get_profile_if_exists(user):
    profile = Profile.objects.filter(user=user)

    if profile.exists():
        return profile.first()

    else:
        return False

def update_or_create_profile(user, profile_data):
    profile, is_created = Profile.objects.get_or_create(user=user)

    profile.full_name = profile_data['full_name']
    profile.phone_no = profile_data['phone_no']
    profile.extra_attribute = {
        'nickname': profile_data['nickname']
    }
    profile.save()

    return profile, is_created

def update_profile(profile, new_data):
    profile.full_name = new_data['full_name']
    profile.phone_no = new_data['phone_no']
    profile.extra_attribute = {
        'nickname': new_data['nickname']
    }
    profile.save()

    return profile

def search_profile(keyword):
    profiles = Profile.objects.filter(
        Q(full_name__icontains=keyword) |
        Q(phone_no__icontains=keyword) |
        Q(extra_attribute__nickname__icontains=keyword)
    ).order_by('-pk')

    return profiles
