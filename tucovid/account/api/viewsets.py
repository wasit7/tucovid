from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from account.api.serializers import UserSerializer
from account.profile import search_profile
from relation.models import Relationship
from django.forms.models import model_to_dict

class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RelationProfileSearchAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response()

    def post(self, request):
        keyword = request.data['keyword']
        profiles = search_profile(keyword)

        reporter_id = None if request.user.is_staff else request.user.pk

        if request.data['reporter_id'] and not reporter_id:
            reporter_id = request.data['reporter_id']

        profiles = [
            profile
            for profile in profiles.exclude(user__pk=reporter_id).exclude(full_name='')[:100]
            if not Relationship.objects \
                .filter(persons__pk=reporter_id) \
                .filter(persons__pk=profile.user.pk) \
                .exists()
        ]

        return Response([
            {
                'id': profile.user.pk,
                'full_name': profile.full_name,
                'phone_no': profile.phone_no,
                'extra_attribute': profile.extra_attribute
            } for profile in profiles[:10]
        ])

class EventProfileSearchAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response()

    def post(self, request):
        keyword = request.data['keyword']

        profiles = search_profile(keyword)
        excluding_ids = []  if request.user.is_staff else [ request.user.pk ]

        if request.data['excluding_ids']:
            excluding_ids += request.data['excluding_ids']

        return Response([
            {
                'id': profile.user.pk,
                'full_name': profile.full_name,
                'phone_no': profile.phone_no,
                'extra_attribute': profile.extra_attribute
            } for profile in profiles.exclude(user__pk__in=excluding_ids).exclude(full_name='')[:10]
        ])
