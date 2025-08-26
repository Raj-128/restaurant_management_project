from django.contrib import admin

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name","phone_number")
    