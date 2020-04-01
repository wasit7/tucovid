from django.urls import path
from rest_framework import routers
from account.api.viewsets import UserViewSet, RelationProfileSearchAPI, EventProfileSearchAPI

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('users/relation/search/', RelationProfileSearchAPI.as_view()),
    path('users/event/search/', EventProfileSearchAPI.as_view()),
]