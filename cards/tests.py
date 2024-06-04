import random
import string
import time
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class CardAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def generate_random_card_data(self):
        card_number = ''.join(random.choices(string.digits, k=16))
        ccv = random.randint(100, 999)

        return {
            'card_number': card_number,
            'ccv': ccv
        }

    def test_card_validation(self):
        valid_card_data = self.generate_random_card_data()
        response = self.client.post('/cards-api/cards/', valid_card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('title', response.data)
        self.assertIn('censored_number', response.data)
        self.assertIn('is_valid', response.data)
        self.assertIn('user', response.data)

    def test_invalid_cards_data(self):
        invalid_cards_data = (
            {
                'card_number': '11223344556677889',
                'ccv': 1034
            },
            {
                'card_number': '1122',
                'ccv': 99
            },
            {
                'card_number': '11223344556677889',
                'ccv': 99
            },
            {
                'card_number': '1122',
                'ccv': 1034
            },
            {
                'card_number': '1122',
                'ccv': 103
            },
            {
                'card_number': '1122334455667788',
                'ccv': 1034
            },
        )

        for data in invalid_cards_data:
            response = self.client.post('/cards-api/cards/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_card_validation_speed(self, expected_duration=35):
        start_time = time.perf_counter()
        for _ in range(100):
            card_data = self.generate_random_card_data()
            response = self.client.post('/cards-api/cards/', card_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        end_time = time.perf_counter()
        duration = end_time - start_time
        self.assertTrue(duration < expected_duration, f"Validation took too long: {duration} seconds")
