from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarsSerializer
from .models import Cars

@api_view(['GET','POST'])  
def cars_list(request):
    
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT'])
def car_detail(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    if request.method == "GET":
        serializer = CarsSerializer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarsSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    