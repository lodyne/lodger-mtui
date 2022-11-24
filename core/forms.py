from django import forms
from core.models import (
    Doctor,
    Patient,
    Appointment
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class DoctorForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = ['firstname','middlename','surname']
        exclude = ['created_at','updated_at']
        
class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ['firstname','middlename','surname','age','gender','phone_number']
        exclude = ['created_at','updated_at']
        
class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ['patient','doctor','appointment_time','appointment_day']
        exclude = ['created_at','updated_at']
        


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']