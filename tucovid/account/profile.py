from account.models import Profile

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
