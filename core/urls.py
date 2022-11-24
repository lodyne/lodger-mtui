from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.home, name='home'),
    
    path('list/doctor',views.listDoctor, name='list_doctor'),
    path('add/doctor', views.addDoctor, name='add_doctor'),
    path('detail/doctor/<int:id>/',views.detailDoctor, name='doctor_detail'),
    path('update/doctor/<int:id>/update',views.updateDoctor, name='doctor_update'),
    path('delete/doctor/<int:id>/delete',views.deleteDoctor, name='doctor_delete'),
    
    path('list/patient',views.listPatient, name='list_patient'),
    path('add/patient', views.addPatient, name='add_patient'),
    path('detail/patient/<int:id>/',views.detailPatient, name='patient_detail'),
    path('update/patient/<int:id>/update',views.updatePatient, name='patient_update'),
    path('delete/patient/<int:id>/delete',views.deletePatient, name='patient_delete'),
    
    path('list/appointment',views.listAppointment, name='list_appointment'),
    path('add/appointment', views.addAppointment, name='add_appointment'),
    path('detail/appointment/<int:id>/',views.detailAppointment, name='appointment_detail'),
    path('update/appointment/<int:id>/update',views.updateAppointment, name='appointment_update'),
    path('delete/appointment/<int:id>/delete',views.deleteAppointment, name='appointment_delete'),
]
