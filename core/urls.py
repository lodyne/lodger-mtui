from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    
    path('',views.home, name='home'),
    
    path('list/doctor',views.listDoctor, name='list_doctor'),
    path('add/doctor', views.addDoctor, name='add_doctor'),
    path('detail/doctor/<int:id>/',views.detailDoctor, name='detail_doctor'),
    path('update/doctor/<int:id>/update',views.updateDoctor, name='update_doctor'),
    path('delete/doctor/<int:id>/delete',views.deleteDoctor, name='delete_doctor'),
    
    path('list/patient',views.listPatient, name='list_patient'),
    path('add/patient', views.addPatient, name='add_patient'),
    path('detail/patient/<int:id>/',views.detailPatient, name='detail_patient'),
    path('update/patient/<int:id>/update',views.updatePatient, name='update_patient'),
    path('delete/patient/<int:id>/delete',views.deletePatient, name='delete_patient'),
    
    path('list/appointment',views.listAppointment, name='list_appointment'),
    path('add/appointment', views.addAppointment, name='add_appointment'),
    path('detail/appointment/<int:id>/',views.detailAppointment, name='detail_appointment'),
    path('update/appointment/<int:id>/update',views.updateAppointment, name='update_appointment'),
    path('delete/appointment/<int:id>/delete',views.deleteAppointment, name='delete_appointment'),
]
