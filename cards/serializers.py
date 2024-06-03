from rest_framework.serializers import ModelSerializer, CharField, IntegerField
from cards.utils import validate_card_number
from cards.models import Card


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardListSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title', 'censored_number', 'is_valid')


class CardCreateSerializer(ModelSerializer):
    card_number = CharField(max_length=16, write_only=True)
    ccv = IntegerField(min_value=100, max_value=999, write_only=True)

    class Meta:
        model = Card
        fields = ('card_number', 'ccv')
        extra_kwargs = {
            'card_number': {'write_only': True},
            'ccv': {'write_only': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        card_number = validated_data.pop('card_number')
        ccv = validated_data.pop('ccv')
        print(validated_data)

        title = f"{user.first_name} {user.last_name}"
        censored_number = f"{card_number[:4]}********{card_number[-4:]}"
        is_valid = validate_card_number(card_number, ccv)

        return Card.objects.create(
            user=user,
            title=title,
            censored_number=censored_number,
            is_valid=is_valid
        )
