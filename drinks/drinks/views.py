#creating end points 
from django.http import JsonResponse 
from .models import Drink 
from .serializers import DrinkSerializer

def drink_list(request):
    #get all the drinks 
    drinks = Drink.objects.all()
    #serialize them 
    serializer = DrinkSerializer(drinks, many =True)
    # turn it into json 

    return JsonResponse(serializer.data, safe=False)

