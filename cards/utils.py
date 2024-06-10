import re


def validate_card_number(card_number: str, ccv: int) -> bool:
    partitions = [int(num) for num in re.findall('.'*2, card_number)]

    for i in range(0, len(partitions), 2):
        check = pow(partitions[i], (partitions[i+1]**3), ccv) % 2 == 0

        if not check:
            return False

    return True
