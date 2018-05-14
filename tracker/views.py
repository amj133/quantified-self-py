from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .models import Meal
from .serializers import FoodSerializer
from .serializers import MealSerializer
from django.http import HttpResponse
import code
# from django.views.decorators.csrf import ensure_csrf_cookie
# @ensure_csrf_cookie

@api_view(['GET', 'DELETE', 'PATCH'])
def get_delete_update_food(request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = FoodSerializer(food)
        return Response(serialized.data)
    elif request.method == 'DELETE':
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        serialized = FoodSerializer(food, data=request.data['food'])
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_foods(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serialized = FoodSerializer(foods, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('food').get('name'),
            'calories': request.data.get('food').get('calories')
        }
        serialized = FoodSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_meals(request):
    if request.method == 'GET':
        meal_id = request.data
        meals = Meal.objects.all()
        serialized = MealSerializer(meals, many=True)
        return Response(serialized.data)

@api_view(['GET'])
def get_meal_foods(request, pk):
    try:
        meal = Meal.objects.get(pk=pk)
    except Meal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = MealSerializer(meal)
        return Response(serialized.data)
