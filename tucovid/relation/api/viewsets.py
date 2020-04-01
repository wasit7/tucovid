from relation.models import Relationship, Event
from relation.api.serializers import RelationshipSerializer, EventSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RelationshipViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EventViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
