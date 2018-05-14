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

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['foods'][0]['name'], 'Banana')
        self.assertEqual(response.data[1]['foods'][0]['name'], 'Avocado')
        self.assertEqual(response.data, serialized.data)

class GetAllFoodsForGivenMealTest(TestCase):

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

    def test_get_all_foods(self):
        response = client.get(reverse('get_meal_foods', kwargs={'pk': 1}))

        meal_and_foods = Meal.objects.get(name='Breakfast')
        serialized = MealSerializer(meal_and_foods)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(meal_and_foods.foods.all()[0].name, 'Banana')
        self.assertEqual(response.data, serialized.data)

    def test_returns_404_if_meal_not_found(self):
        response = client.get(reverse('get_meal_foods', kwargs={'pk': 12}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class AssociatesFoodWithMeal(TestCase):

    def setUp(self):
        breakfast = Meal.objects.create(name='Breakfast')
        banana = Food.objects.create(
            name='Banana',
            calories=140
        )
        twizzler = Food.objects.create(
            name='Twizzler',
            calories=240
        )
        breakfast.foods.add(banana)


    def test_adds_food_to_meal(self):
        breakfast = Meal.objects.get(name='Breakfast')
        self.assertEqual(breakfast.foods.all().__len__(), 1)

        response = client.post(reverse('post_meal_foods', kwargs={'meal_pk': 1, 'food_pk': 2}))
        breakfast = Meal.objects.get(name='Breakfast')
        serialized = MealSerializer(breakfast)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Successfully added Twizzler to Breakfast')
        self.assertEqual(breakfast.foods.all().__len__(), 2)
