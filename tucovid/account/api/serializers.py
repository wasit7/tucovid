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
            'full_name',
            'phone_no',
            'extra_attribute'
        ]

    def get_full_name(self, obj):
        return obj.profile.full_name

    def get_phone_no(self, obj):
        return obj.profile.phone_no

    def get_extra_attribute(self, obj):
        return obj.profile.extra_attribute

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id',
            'full_name',
            'phone_no',
            'extra_attribute'
        ]

    def get_id(self, obj):
        return obj.user.pk
