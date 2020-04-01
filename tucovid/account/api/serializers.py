from account.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'full_name',
            'phone_no',
            'extra_attribute'
        ]
