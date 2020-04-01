from relation.models import Relationship, Event
from rest_framework import serializers
from account.api.serializers import UserSerializer
from django.contrib.auth.models import User

class RelationshipSerializer(serializers.ModelSerializer):
    persons = UserSerializer(many=True)
    level = serializers.SerializerMethodField()
    created_by = UserSerializer()

    class Meta:
        model = Relationship
        fields = [
            'persons',
            'level',
            'created_date',
            'created_by'
        ]

    def get_level(self, obj):
        return obj.get_level_display()

class EventSerializer(serializers.ModelSerializer):
    reporter = UserSerializer()
    participants = UserSerializer(many=True)
    created_by = UserSerializer()

    class Meta:
        model = Event
        fields = [
            'title',
            'start',
            'finish',
            'location',
            'reporter',
            'participants',
            'created_date',
            'created_by'
        ]

class UserRelationshipSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    other_person = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()

    class Meta:
        model = Relationship
        fields = [
            'id',
            'other_person',
            'level'
        ]

    def get_id(self, obj):
        return obj.pk

    def get_other_person(self, obj):
        user = self.context['request'].user

        return obj.persons.exclude(pk=user.pk).first().profile.full_name

    def get_level(self, obj):
        return obj.get_level_display()

class UserEventSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    reporter = serializers.SerializerMethodField()
    start = serializers.DateTimeField(format="%-d %b %Y %H:%M")
    finish = serializers.DateTimeField(format="%-d %b %Y %H:%M")
    participants = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'start',
            'finish',
            'location',
            'reporter',
            'participants'
        ]

    def get_id(self, obj):
        return obj.pk

    def get_reporter(self, obj):
        return {
            'name': obj.reporter.profile.full_name
        }

    def get_participants(self, obj):
        return [
            {
                'name': participant.profile.full_name
            } for participant in obj.participants.all()
        ]
