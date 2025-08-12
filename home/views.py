from django.shortcuts import render
from .models import *

# Create your views here.
 
def home_view(request):
    restaurant = Restaurant.objects.first()
    return render(request , 'home.html',{'restaurant':restaurant})

def about_view(request):
    return render(request,'about.html')    

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Message from {name} ({email}):{message}")    
    return render(request,'contact.html')    