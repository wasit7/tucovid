from rest_framework import routers
from relation.api.viewsets import RelationshipViewSet

router = routers.SimpleRouter()
router.register(r'relationships', RelationshipViewSet)

urlpatterns = router.urls
