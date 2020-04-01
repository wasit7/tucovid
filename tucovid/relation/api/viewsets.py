from relation.models import Relationship
from relation.api.serializers import RelationshipSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RelationshipViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
