from django.shortcuts import render,redirect

from core.forms import (
    DoctorForm,
    PatientForm,
    AppointmentForm
)

from core.models import (
    Doctor,
    Patient,
    Appointment
)

from django.contrib.auth.decorators import login_required

# Create your views here.

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
                return redirect('core:add_doctor')

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
            return redirect('core:list_doctor')
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
        return redirect('core:list_doctor')
    
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
                return redirect('core:list_patient')

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
            return redirect('core:list_patient')
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
        return redirect('core:list_patient')
    
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

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('core:list_appointment')

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
            return redirect('core:list_appointment')
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
        return redirect('core:list_appointment')
    
    context = {
        'appointment': appointment
    }
    
    template_name = 'appointment/delete_appointment.html'
    
    return render(request,template_name, context)
