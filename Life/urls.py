from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="life/index.html"),name="index"),
    path('doctors/', views.DoctorListView.as_view(), name="doctors"),
    path('departments/', views.DepartmentListView.as_view(), name="departments"),
    path('departments/<int:dept_id>', views.DepartmentDetails, name="department_detail"),
    path('register/doctor',views.PostDoctor,name='add_doctor' ),
    path('register/patient',views.PostPatient,name='add_patient'),
    path('login/doctor', views.LoginDoctor,name='authenticate_doctor'),
    path('login/patient', views.LoginPatient,name='authenticate_patient'),
    path('patient/<str:patient_id>',views.PatientDetails,name='patient_details'),
    path('doctor/<str:doctor_id>',views.DoctorDetails,name='doctor_details'),
]