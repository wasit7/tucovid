from relation.models import Relationship
from rest_framework import serializers
from account.api.serializers import ProfileSerializer
from django.db.models import F

class RelationshipSerializer(serializers.ModelSerializer):
    persons = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()

    class Meta:
        model = Relationship
        fields = [
            'persons',
            'level',
            'created_date',
            'created_by'
        ]

    def get_persons(self, obj):
        persons = obj.persons.all()
        profiles = [ person.profile.__dict__ for person in persons ]
        serializer = ProfileSerializer(data=profiles, many=True)

        if serializer.is_valid():
            return serializer.data
        else:
            return []

    def get_level(self, obj):
        return obj.get_level_display()
