from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from cards.serializers import CardSerializer, CardListSerializer, CardCreateSerializer
from cards.utils import SerializerFactory
from cards.models import Card


class CardViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = SerializerFactory(
        default=CardSerializer,
        list=CardListSerializer,
        create=CardCreateSerializer,
    )
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('created_at',)
    # We can also order by id, which will do the same thing as created_at, but faster.

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
