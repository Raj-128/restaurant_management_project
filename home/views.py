from django.shortcuts import render
from .models import *
# Create your views here.
 
def home_view(request):
    restaurant = None
    error_messsage = None

    try:
        restaurant = Restaurant.objects.first()
        if not restaurant:
            error_messsage = "No restaurant data found."
    except DatabaseError as e:
        error_messsage = f"Database error occured: {e}"
    except Exception as e:
        error_messsage = f"An unexpected error occured: {e}"
    return render(request , 'home.html',{'restaurant':restaurant,'error_message':error_message})

def about_view(request):
    return render(request,'about.html')    

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Message from {name} ({email}):{message}")    
    return render(request,'contact.html')    

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
