from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Doctor,Department,Patient,Appointment
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import PostForm_Doctor,PostForm_Patient
# Create your views here.

class DoctorListView(ListView):
    template_name = 'life/team.html'
    queryset = Doctor.objects.all()
    paginate_by = 8

class DepartmentListView(ListView):
    template_name='life/department.html'
    queryset= Department.objects.all()

def DepartmentDetails(request,dept_id):
     department=get_object_or_404(Department,pk=dept_id)
     doctors=department.doctor_set.all()    

     return render(request,'life/department_details.html',{'department':department,
                                                           'doctors':doctors                     
                                                        })

def PostDoctor(request):
        if request.method=="POST":
                form=PostForm_Doctor(request.POST, request.FILES)
                EIDS= [doctor.eid for doctor in Doctor.objects.all()]

                if(EIDS==[]):
                        EID=['D100',]

                last_eid= sorted(EIDS)[len(EIDS)-1]
                cur_eid= int(last_eid[1:])+1

                if(cur_eid)<9:
                        eid='D'+ '0'+str(cur_eid)
                else:
                        eid= 'D' +str(cur_eid)

                if form.is_valid():
                        post=form.save(commit=False)
                        post.eid=eid
                        post.save()
                        User.objects.create_user(username=eid,password=form.cleaned_data.get('password'))
                        print(request.POST)
                        html = "<html><body>It is now</body></html>"
                        return HttpResponse(html)
                else:   
                        print(form.errors)
                        html = "<html><body>It nbnjkbhis now</body></html>"
                        return HttpResponse(html)           
        else:
                form=PostForm_Doctor()
                return render(request,'life/doctor_signup.html',{'form':form})

def PostPatient(request):
        if request.method=="POST":
                form=PostForm_Patient(request.POST)
                PIDS= [patient.pid for patient in Patient.objects.all()]

                if(PIDS==[]):
                        PIDS=['P100',]

                last_pid= sorted(PIDS)[len(PIDS)-1]
                cur_pid= int(last_pid[1:])+1

                if(cur_pid)<9:
                        pid= 'P'+'0'+str(cur_pid)
                else:
                        pid= 'P'+str(cur_pid)

                if form.is_valid():
                        post=form.save(commit=False)
                        post.pid=pid
                        post.save()
                        User.objects.create_user(username=pid,password=form.cleaned_data.get('password'))
                        print(request.POST)
                        html = "<html><body>It is now</body></html>"
                        return HttpResponse(html)
                else:   
                        print(form.errors)
                        html = "<html><body>It nbnjkbhis now</body></html>"
                        return HttpResponse(html)           
        else:
                form=PostForm_Patient()
                return render(request,'life/patient_signup.html',{'form':form})

def LoginDoctor(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)

                if(username[0]=='P'):
                        error= "*Your account was inactive."
                        return render(request,'life/doctor_login.html',{'error': error})

                if user:
                        if user.is_active:
                                return redirect('/doctor/'+username)
                        else:   
                                error= "*Your account was inactive."
                                return render(request,'life/doctor_login.html',{'error': error})
                else:
                        error='*Invalid Username and/or password'
                        return render(request,'life/doctor_login.html',{'error': error})
        else:   
                error=''
                return render(request,'life/doctor_login.html',{'error': error})

def LoginPatient(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)

                if(username[0]=='D'):
                        error= "*Your account was inactive."
                        return render(request,'life/patient_login.html',{'error': error})

                if user:
                        if user.is_active:
                                return redirect('/patient/'+username)
                        else:   
                                error= "*Your account was inactive."
                                return render(request,'life/patient_login.html',{'error': error})
                else:
                        error='*Invalid Username and/or password'
                        return render(request,'life/patient_login.html',{'error': error})
        else:   
                error=''
                return render(request,'life/patient_login.html',{'error': error})

def DoctorDetails(request,doctor_id):
     doctor=get_object_or_404(Doctor,pk=doctor_id)
     appointments=Appointment.objects.all().filter(dname=doctor)    

     return render(request,'life/doctor_details.html',{'doctor':doctor,
                                                           'appointments':appointments                     
                                                        })


def PatientDetails(request,patient_id):
     patient=get_object_or_404(Patient,pk=patient_id)
     appointments=Appointment.objects.all().filter(pname=patient)    

     return render(request,'life/patient_details.html',{'patient':patient,
                                                           'appointments':appointments                     
                                                        })