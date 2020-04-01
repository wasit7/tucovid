from rest_framework import routers
from relation.api.viewsets import (
    RelationshipViewSet,
    EventViewSet,
    UserRelationshipViewSet,
    UserEventViewSet
)

router = routers.SimpleRouter()
router.register(r'relationships', RelationshipViewSet)
router.register(r'events', EventViewSet)
router.register(prefix=r'users/(?P<user_id>\d+)/relationships', viewset=UserRelationshipViewSet)
router.register(prefix=r'users/(?P<user_id>\d+)/events', viewset=UserEventViewSet)

urlpatterns = router.urls
