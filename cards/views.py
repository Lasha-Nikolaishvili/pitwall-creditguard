from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
