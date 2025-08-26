from django.shortcuts import render , redirect
from home.models import *
from orders.models import *
from products.models import *
from products.models import *
from django.db import models
# Create your views here.
 
def home_view(request):
    query = request.GET.get("q")
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    restaurant = None
    menu_items = Menu.objects.all()
    error_messsage = None
    address = "123 main Street, Ahemdabad,Gujarat,India"
    context = {"address":address}
    location = RestaurantLocation.objects.first()
    try:
        restaurant = Restaurant.objects.first()
        if not restaurant:
            error_messsage = "No restaurant data found."
    except DatabaseError as e:
        error_messsage = f"Database error occured: {e}"
    except Exception as e:
        error_messsage = f"An unexpected error occured: {e}"
    return render(request , 'home.html',{'restaurant':restaurant,'error_message':error_message,'menu_items':menu_items,'location':location,"query":query})

def about_view(request):
    return render(request,'about.html')    

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
            
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})        print(f"Message from {name} ({email}):{message}")   

def menu_list(request):
    menu_items = [
        {"name":" Margherita Pizza","price": 299,"description":"Classic Pizza with tomato and Mozzarella" },
        {"name":"Veg Burger","price":199,"desciption":"Loaded with fresh veggies and cheese"},
        {"name":"Pasta Alfredo","price":249,"description":"Creamy white sauce pasta"},
        {"name":"Cold Coffee","price":99,"description":"Refreshing chilled coffee"},
]
    return render(request,'menu_list.html',{"menu_items":menu_items})

def feedback_view(request):
    if request.method =="POST":
        name = request.POST.get("name")
        comments = request.POST.get("comments")

        if name and comments:
            Feedback.objects.create(name=name, comments=comments)
            return redirect('feedback')

    return render(request,'feedback.html')        
