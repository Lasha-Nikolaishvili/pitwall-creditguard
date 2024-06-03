from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from cards.serializers import CardSerializer, CardCreateSerializer
from cards.permissions import IsOwner
from cards.utils import SerializerFactory
from cards.models import Card


class CardViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = SerializerFactory(
        default=CardSerializer,
        create=CardCreateSerializer,
    )
    permission_classes = [IsOwner]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('created_at',)
    # We could also order by id, which will do the same thing as created_at, but faster.

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
