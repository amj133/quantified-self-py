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
