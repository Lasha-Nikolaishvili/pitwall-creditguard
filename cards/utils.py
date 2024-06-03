from rest_framework.views import APIView


class SerializerGetter:
    def __init__(self, default, **kwargs):
        self.default = default
        self.serializer_per_action = kwargs

    def get_serializer_class(self, view: [APIView]):
        return self.serializer_per_action.get(
            getattr(view, 'action', None),
            self.default
        )

    def __call__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        view: APIView = context.get('view', None)
        serializer_class = self.get_serializer_class(view)
        return serializer_class(*args, **kwargs)


class SerializerFactory:
    def __init__(self, default, **kwargs):
        self.serializer_getter = SerializerGetter(
            default=default, **kwargs,
        )

    def __call__(self, *args, **kwargs):
        return self.serializer_getter(*args, **kwargs)


def validate_card_number(card_number: str, ccv: int) -> bool:
    partitions = (
        (card_number[:2], card_number[2:4]),
        (card_number[4:6], card_number[6:8]),
        (card_number[8:10], card_number[10:12]),
        (card_number[12:14], card_number[14:16])
    )

    for x, y in partitions:
        check = (int(x)**(int(y)**3)) % ccv % 2 == 0
        if not check:
            return False

    return True
