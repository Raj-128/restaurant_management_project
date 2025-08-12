from django.urls import path
from .views import *

urlpatterns = [
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name="contact"),
    path('menu/',views.menu_list,name='menu_list'),

    )
]