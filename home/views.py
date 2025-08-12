from django.shortcuts import render
from .models import *

# Create your views here.
 
def home_view(request):
    restaurant = Restaurant.objects.first()
    return render(request , 'home.html',{'restaurant':restaurant})

def about_view(request):
    return render(request,'about.html')    

def contact_view(request):
    return render(request,'contact.html')    