from django.shortcuts import render,redirect

from django.contrib import messages

from core.forms import (
    DoctorForm,
    PatientForm,
    AppointmentForm,
    UserRegisterForm
)

from core.models import (
    Doctor,
    Patient,
    Appointment
)

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def listDoctor(request):
    
    doctors = Doctor.objects.all()
    
    context = {
        'doctors':doctors
    }
    
    template_name = 'doctor/list_doctor.html',
    
    return render(request,template_name, context)

# * Detail doctor
@login_required
def detailDoctor(request,id):
    doctor = Doctor.objects.get(id = id)
    
    context = {
        'doctor':doctor
    }
    
    template_name = 'doctor/detail_doctor.html'
    
    return render(request,template_name,context)
    

# * Create doctors
@login_required
def addDoctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_doctor')

            except Exception as err:
                print(err)
        else:
            print(form.errors)            
    else:
        form = DoctorForm()
        
    context = {
        'form':form
    }
    
    template_name = 'doctor/add_doctor.html'
    
    return render(request,template_name,context)

# * Update doctor
@login_required
def updateDoctor(request,id):
    doctors = Doctor.objects.get(id = id)
    if request.method == 'POST':

        form = DoctorForm(request.POST,request.FILES, instance=doctors)
        if form.is_valid():
            form.save()
            return redirect('list_doctor')
    else:
        form = DoctorForm(instance=doctors)

    context = {
        'form': form
    }
    
    template_name = 'doctor/edit_doctor.html'

    return render(request,template_name,context)

# * Delete doctor
@login_required
def deleteDoctor(request,id):
    doctor = Doctor.objects.get(id = id)
    
    if request.method == 'POST':
        doctor.delete()
        return redirect('list_doctor')
    
    context = {
        'doctor': doctor
    }
    
    template_name = 'doctor/delete_doctor.html'
    
    return render(request,template_name, context)


@login_required
def listPatient(request):
    
    patients = Patient.objects.all()
    
    context = {
        'patients':patients
    }
    
    template_name = 'patient/list_patient.html',
    
    return render(request,template_name, context)

# * Detail Patient
@login_required
def detailPatient(request,id):
    patient = Patient.objects.get(id = id)
    
    context = {
        'Patient':Patient
    }
    
    template_name = 'patient/detail_patient.html'
    
    return render(request,template_name,context)
    

# * Create Patients
@login_required
def addPatient(request):

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_patient')

            except Exception as err:
                print(err)
        else:
            print(form.errors)            
    else:
        form = PatientForm()
        
    context = {
        'form':form
    }
    
    template_name = 'patient/add_patient.html'
    
    return render(request,template_name,context)

# * Update Patient
@login_required
def updatePatient(request,id):
    patients = Patient.objects.get(id = id)
    if request.method == 'POST':

        form = PatientForm(request.POST,request.FILES, instance=patients)
        if form.is_valid():
            form.save()
            return redirect('list_patient')
    else:
        form = PatientForm(instance=patients)

    context = {
        'form': form
    }
    
    template_name = 'patient/edit_patient.html'

    return render(request,template_name,context)

# * Delete Patient
@login_required
def deletePatient(request,id):
    patient = Patient.objects.get(id = id)
    
    if request.method == 'POST':
        patient.delete()
        return redirect('list_patient')
    
    context = {
        'patient': patient
    }
    
    template_name = 'patient/delete_patient.html'
    
    return render(request,template_name, context)

@login_required
def listAppointment(request):
    
    appointments = Appointment.objects.all()
    
    context = {
        'appointments':appointments
    }
    
    template_name = 'appointment/list_appointment.html',
    
    return render(request,template_name, context)

# * Detail Appointment
@login_required
def detailAppointment(request,id):
    appointment = Appointment.objects.get(id = id)
    
    context = {
        'appointment':appointment
    }
    
    template_name = 'appointment/detail_appointment.html'
    
    return render(request,template_name,context)
    

# * Create Appointments
@login_required
def addAppointment(request):
    patient = Patient.objects.filter(id=form.patient.id).first()
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.patient.save()
                form.save()
                
                return redirect('list_appointment')

            except Exception as err:
                print(err)
        else:
            print(form.errors)            
    else:
        form = AppointmentForm()
        
    context = {
        'form':form
    }
    
    template_name = 'appointment/add_appointment.html'
    
    return render(request,template_name,context)

# * Update Appointment
@login_required
def updateAppointment(request,id):
    appointments = Appointment.objects.get(id = id)
    if request.method == 'POST':

        form = AppointmentForm(request.POST,request.FILES, instance=appointments)
        if form.is_valid():
            form.save()
            return redirect('list_appointment')
    else:
        form = AppointmentForm(instance=appointments)

    context = {
        'form': form
    }
    
    template_name = 'appointment/edit_appointment.html'

    return render(request,template_name,context)

# * Delete Appointment
@login_required
def deleteAppointment(request,id):
    appointment = appointment.objects.get(id = id)
    
    if request.method == 'POST':
        appointment.delete()
        return redirect('list_appointment')
    
    context = {
        'appointment': appointment
    }
    
    template_name = 'appointment/delete_appointment.html'
    
    return render(request,template_name, context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Hi {username}, you have been created an account. Login now")
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)