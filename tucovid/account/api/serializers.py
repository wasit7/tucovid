from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Profile

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phone_no = serializers.SerializerMethodField()
    extra_attribute = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'phone_no',
            'extra_attribute'
        ]

    def get_full_name(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.full_name

        return None

    def get_phone_no(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.phone_no

        return None

    def get_extra_attribute(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.extra_attribute

        return None
