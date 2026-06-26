from django.contrib import admin
from .models import Restaurant, Chef, TableBooking, ChefBooking, Staff

# Register Restaurant
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine', 'location']
    search_fields = ['name', 'cuisine']
    list_filter = ['cuisine']

# Register Chef
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['name', 'signature_dish', 'cuisine']
    search_fields = ['name']

# Register TableBooking (Already there)
@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'restaurant', 'date', 'time', 'guests', 'status']
    list_filter = ['status', 'date', 'restaurant']
    search_fields = ['name', 'email']

# Register ChefBooking
@admin.register(ChefBooking)
class ChefBookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'chef', 'date', 'time', 'status']
    list_filter = ['status', 'date']

# Register Staff (Optional)
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone']