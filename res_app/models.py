from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurants/')
    location = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)

    @property
    def default_image(self):
        images = {
            "Udupi Garden": "images/udupi.jpg",
            "Soofi Mandi": "images/soofi.jpg",
            "Rameshwaram Cafe": "images/ramesggg.jpg",
            "Onesta": "images/onesta.jpg",
        }
        return images.get(self.name, "images/udupi.jpg")

    def __str__(self):
        return self.name

class Chef(models.Model):
    name = models.CharField(max_length=100)
    signature_dish = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to='chefs/')
    bio = models.TextField(blank=True)

    @property
    def default_image(self):
        images = {
            "Chef Sanjeev Kapoor": "images/san.jpeg",
            "Chef Venkatesh Bhatt": "images/venkatesh.avif",
            "Chef Ranveer Brar": "images/brar.jpg",
            "Chef Koushik S. A.K.A.": "images/Chef Koushik.jpg",
        }
        return images.get(self.name, "images/san.jpeg")

    def __str__(self):
        return self.name

class TableBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} ({self.status})"

class ChefBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.chef.name}"

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
