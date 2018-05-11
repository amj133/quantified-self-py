from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world.  Your're at the calorie tracker index!!!")

def foods(request):
    response = "You're looking at the foods index."
    return HttpResponse(response)

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
        return Response({})
    elif request.method == 'PATCH':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_foods(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serialized = FoodSerializer(foods, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        return Response({})
