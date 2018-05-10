from django.test import TestCase
from ..models import Food

class FoodTest(TestCase):

    def setUp(self):
        Food.objects.create(
            name='Banana',
            calories='140'
        )
        Food.objects.create(
            name='Twizzler',
            calories='240'
        )

    def test_food_attrs(self):
        banana = Food.objects.get(name='Banana')
        twizzler = Food.objects.get(name='Twizzler')
        
        self.assertEqual(banana.calories, 140)
        self.assertEqual(twizzler.calories, 240)
