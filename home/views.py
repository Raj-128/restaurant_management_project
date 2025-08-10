from django.shortcuts import render
from .models import *

# Create your views here.
 
 def home_view(request):
    restaurant = Restaurant.objects.first()
    return render(request , 'home.html',{'restaurant':restaurant})