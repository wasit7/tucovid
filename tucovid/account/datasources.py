def map_profile(profile):
    return {
        'id': profile.user.pk,
        'full_name': profile.full_name,
        'phone_no': profile.phone_no,
        'extra_attribute': profile.extra_attribute
    }
