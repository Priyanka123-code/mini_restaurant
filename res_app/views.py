from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Chef, TableBooking, ChefBooking
from .forms import TableBookingForm, ChefBookingForm
from .default_content import ensure_default_content

def home(request):
    ensure_default_content()
    restaurants = Restaurant.objects.all()
    chefs = Chef.objects.all()[:4]
    return render(request, 'home.html', {'restaurants': restaurants, 'chefs': chefs})

def restaurant_list(request):
    ensure_default_content()
    restaurants = Restaurant.objects.all()
    return render(request, 'rest.html', {'restaurants': restaurants})

def chef_list(request):
    ensure_default_content()
    chefs = Chef.objects.all()
    return render(request, 'chef.html', {'chefs': chefs})

def book_table(request):
    ensure_default_content()
    if request.method == "POST":
        form = TableBookingForm(request.POST)
        if form.is_valid():
            form.save()                    # ← Save to MySQL
            return redirect('booking_success')
        else:
            print(form.errors)             # For debugging
    else:
        form = TableBookingForm()
    
    return render(request, 'booktable.html', {'form': form})

def book_chef(request, chef_id):
    ensure_default_content()
    chef = get_object_or_404(Chef, id=chef_id)
    if request.method == 'POST':
        form = ChefBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.chef = chef
            booking.save()
            return redirect('booking_success')
    else:
        form = ChefBookingForm()
    return render(request, 'bookchef.html', {'form': form, 'chef': chef})

def booking_success(request):
    return render(request, 'sucess.html')

def staff_login(request):
    return render(request, 'staff_login.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')
