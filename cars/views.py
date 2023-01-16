from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarsSerializer
from .models import Cars

@api_view(['GET', 'POST'])  
def cars_list(request):
    
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'Post':
        pass