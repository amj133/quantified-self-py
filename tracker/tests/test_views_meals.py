import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Food
from ..models import Meal
# from ..serializers import FoodSerializer
from ..serializers import MealSerializer
import code

client = Client()

class GetAllMealsTest(TestCase):

    def setUp(self):
        breakfast = Meal.objects.create(name='Breakfast')
        lunch = Meal.objects.create(name='Lunch')
        banana = Food.objects.create(
            name='Banana',
            calories=140
        )
        twizzler = Food.objects.create(
            name='Twizzler',
            calories=240
        )
        avocado = Food.objects.create(
            name='Avocado',
            calories=340
        )
        breakfast.foods.add(banana)
        breakfast.foods.add(twizzler)
        lunch.foods.add(avocado)


    def test_get_all_meals(self):
        response = client.get(reverse('get_meals'))

        meals = Meal.objects.all()
        serialized = MealSerializer(meals, many=True)

        # code.interact(local=dict(globals(), **locals()))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['foods'][0]['name'], 'Banana')
        self.assertEqual(response.data[1]['foods'][0]['name'], 'Avocado')
        self.assertEqual(response.data, serialized.data)
