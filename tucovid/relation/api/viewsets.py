from relation.models import Relationship, Event
from relation.api.serializers import (
    RelationshipSerializer,
    EventSerializer,
    UserRelationshipSerializer,
    UserEventSerializer
)
from relation.api.permissions import IsOwnerOrStaff
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.db.models import Q

class RelationshipViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EventViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserRelationshipViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Relationship.objects.all()
    serializer_class = UserRelationshipSerializer
    permission_classes = [IsOwnerOrStaff]

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['user_id'])
        return Relationship.objects.filter(persons=user).order_by('-id')

class UserEventViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Event.objects.all()
    serializer_class = UserEventSerializer
    permission_classes = [IsOwnerOrStaff]

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['user_id'])
        return Event.objects.filter(
            Q(reporter=user) |
            Q(participants=user)
        ).distinct('id').order_by('-id')
