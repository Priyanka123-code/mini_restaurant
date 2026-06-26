from django import forms
from .models import TableBooking, ChefBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name', 'email', 'phone', 'restaurant', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ChefBookingForm(forms.ModelForm):
    class Meta:
        model = ChefBooking
        fields = ['name', 'email', 'date', 'time', 'people', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }