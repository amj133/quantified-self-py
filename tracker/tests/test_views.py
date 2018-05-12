import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Food
from ..serializers import FoodSerializer
import code

client = Client()

class GetAllFoodsTest(TestCase):

    def setUp(self):
        Food.objects.create(
            name='Banana',
            calories=140
        )
        Food.objects.create(
            name='Twizzler',
            calories=240
        )
        Food.objects.create(
            name='Avocado',
            calories=340
        )

    def test_get_all_foods(self):
        response = client.get(reverse('get_post_foods'))

        foods = Food.objects.all()
        serialized = FoodSerializer(foods, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

class GetSingleFoodTest(TestCase):

    def setUp(self):
        Food.objects.create(
            name='Banana',
            calories=140
        )
        Food.objects.create(
            name='Twizzler',
            calories=240
        )

    def test_get_single_food(self):
        response = client.get(reverse('get_delete_update_food', kwargs={'pk': 1}))

        food = Food.objects.get(pk=1)
        serialized = FoodSerializer(food)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)

    def test_returns_404_if_food_not_found(self):
        response = client.get(reverse('get_delete_update_food', kwargs={'pk': 4}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateFoodTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            "food": {
                "name": "Mint",
                "calories": "225"
            }
        }
        self.invalid_payload_1 = {
            "food" : {
                "name": "Mint"
            }
        }
        self.invalid_payload_2 = {
            "food" : {
                "calories": "225"
            }
        }

    def test_creates_food(self):
        response = client.post(
            reverse('get_post_foods'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        food = Food.objects.get(pk=1)
        serialized = FoodSerializer(food)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serialized.data)

    def test_does_not_create_food_with_no_calories(self):
        response = client.post(
            reverse('get_post_foods'),
            data=json.dumps(self.invalid_payload_1),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_does_not_create_food_with_no_name(self):
        response = client.post(
            reverse('get_post_foods'),
            data=json.dumps(self.invalid_payload_2),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateFoodTest(TestCase):

    def setUp(self):
        Food.objects.create(
            name='Banana',
            calories=140
        )
        self.valid_payload = {
            'food': {
                'name': 'Naner',
                'calories': 145
            }
        }

    def test_edits_food(self):
        response = client.patch(
            reverse('get_delete_update_food', kwargs={'pk': 1}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
            )
        food = Food.objects.get(pk=1)
        serialized = FoodSerializer(food)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data, serialized.data)

    def test_returns_404_if_food_not_found(self):
        response = client.patch(
            reverse('get_delete_update_food', kwargs={'pk': 2}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
            )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class DeleteFoodTest(TestCase):

    def setUp(self):
        Food.objects.create(
            name='Banana',
            calories=140
        )
        Food.objects.create(
            name='Avocado',
            calories=240
        )

    def test_deletes_food(self):
        response = client.delete(reverse('get_delete_update_food', kwargs={'pk': 2}))

        foods = Food.objects.all()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(foods.count(), 1)

    def test_returns_404_if_food_not_found(self):
        response = client.delete(reverse('get_delete_update_food', kwargs={'pk': 3}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
