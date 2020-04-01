from rest_framework import routers
from account.api.viewsets import ProfileViewSet

router = routers.SimpleRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = router.urls
