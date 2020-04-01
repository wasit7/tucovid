from rest_framework import routers
from relation.api.viewsets import RelationshipViewSet, EventViewSet

router = routers.SimpleRouter()
router.register(r'relationships', RelationshipViewSet)
router.register(r'events', EventViewSet)

urlpatterns = router.urls
