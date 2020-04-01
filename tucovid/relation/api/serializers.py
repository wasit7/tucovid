from relation.models import Relationship, Event
from rest_framework import serializers
from account.api.serializers import UserSerializer

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
