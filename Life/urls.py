from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('contact/',TemplateView.as_view(template_name='life/contacts.html'),name="call"),
    path('gallery/',TemplateView.as_view(template_name='life/gallery.html'),name="gallery"),
    path('', TemplateView.as_view(template_name="life/index.html"),name="index"),
    path('doctors/', views.DoctorListView.as_view(), name="doctors"),
    path('departments/', views.DepartmentListView.as_view(), name="departments"),
    path('departments/<int:dept_id>', views.DepartmentDetails, name="department_detail"),
    path('register/<str:usertype>',views.PostUser,name='add_user' ),
    path('login/<str:usertype>/<int:msg>', views.LoginUser,name='authenticate'),
    path('patient/<str:patient_id>',views.PatientDetails,name='patient_details'),
    path('doctor/<str:doctor_id>',views.DoctorDetails,name='doctor_details'),
    path('logout/',views.Logout,name='logout')
]