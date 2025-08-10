from django.shortcuts import render
from django.conf import settings

# Create your views here.
 
 def home_view(request):
    resetaurant_name = getattr(models,'RESTAURANT_NAME','my_restaurant')
    return render(request , 'home.html',{'restaurant_name':restaurant_name})