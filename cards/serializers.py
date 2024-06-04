from rest_framework.serializers import ModelSerializer, CharField, IntegerField
from cards.utils import validate_card_number
from cards.models import Card


class CardSerializer(ModelSerializer):
    card_number = CharField(min_length=16, max_length=16, write_only=True)
    ccv = IntegerField(min_value=100, max_value=999, write_only=True)

    class Meta:
        model = Card
        fields = ('id', 'user', 'title', 'censored_number', 'is_valid', 'created_at', 'card_number', 'ccv')
        read_only_fields = ('user', 'title', 'censored_number', 'is_valid')
        extra_kwargs = {
            'card_number': {'write_only': True},
            'ccv': {'write_only': True},
        }

    def create(self, validated_data):
        user = self.context['request'].user
        card_number = validated_data.pop('card_number')
        ccv = validated_data.pop('ccv')

        title = f"{user.first_name} {user.last_name}"
        censored_number = f"{card_number[:4]}********{card_number[-4:]}"
        is_valid = validate_card_number(card_number, ccv)

        return Card.objects.create(
            user=user,
            title=title,
            censored_number=censored_number,
            is_valid=is_valid
        )
