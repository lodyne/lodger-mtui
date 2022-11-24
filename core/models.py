from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Patient(models.Model):
    
    GENDER = [
		('male', 'Male'),
		('female', 'Female'),
	]
    
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=50, choices = GENDER)
    address = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    

    def __str__(self):
        return (f"{self.firstname} {self.surname}")
    

class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    
    

    def __str__(self):
        return (f"{self.firstname} {self.surname}")
    
class Appointment(models.Model):
    APPOINTMENT_DAYS = (
        ('Monday','Monday'),
        ('Tuesday','Monday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday')
    )
    patient = models.ForeignKey(Patient, related_name ='patient_appointment' ,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name ='doctor_appointment', on_delete=models.CASCADE)
    appointment_time = models.TimeField(auto_now=False, auto_now_add=False)
    appointment_day = models.CharField(max_length=10, choices=APPOINTMENT_DAYS)
    
    def __str__(self):
        return (f"{self.patient.firstname} {self.patient.surname}")

   

