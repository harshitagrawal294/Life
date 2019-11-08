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
from .forms import PostForm_Doctor,PostForm_Patient,Appointment_form
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,user_passes_test

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

def PostUser(request,usertype):

        if request.method=="POST":

                if(usertype=='doctor'):
                        Model=Doctor
                        form=PostForm_Doctor(request.POST, request.FILES)
                        id='D'
                else:
                        Model=Patient
                        form=PostForm_Patient(request.POST,request.FILES)
                        id='P'




                UIDS= [User.pk for User in Model.objects.all()]
                print(UIDS)

                if(UIDS==[]):
                        UID=[id+ '100',]

                last_uid= sorted(UIDS)[len(UIDS)-1]
                cur_uid= int(last_uid[1:])+1

                if(cur_uid)<9:
                        uid=id+ '0'+str(cur_uid)
                else:
                        uid= id +str(cur_uid)

                if form.is_valid():
                        post=form.save(commit=False)
                        post.pk=uid
                        post.save()
                        username=uid
                        password=form.cleaned_data.get('password')
                        User.objects.create_user(username=username,password=password)
                        user = authenticate(username=username, password=password)
                        login(request, user)
                        return redirect('/{}/'.format(usertype)+username)
                else:   
                        return render(request,'life/user_signup.html',{'form':form})        
        else:

                if(usertype=='doctor'):
                        form=PostForm_Doctor()
                else:
                        form=PostForm_Patient()
                return render(request,'life/user_signup.html',{'form':form})


def LoginDoctor(request,msg):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)

                if(username[0]=='P'):
                        error= "*Your account was inactive."
                        return render(request,'life/doctor_login.html',{'error': error})

                if user:
                        if user.is_active:
                                login(request, user)
                                return redirect('/doctor/'+username)
                        else:   
                                error= "*Your account was inactive."
                                return render(request,'life/doctor_login.html',{'error': error})
                else:
                        error='*Invalid Username and/or password'
                        return render(request,'life/doctor_login.html',{'error': error})
        else:   
                error=''
                if(msg==2):
                        error='You are successfully logged out'
                return render(request,'life/doctor_login.html',{'error': error})

def LoginPatient(request,msg):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)

                if(username[0]=='D'):
                        error= "*Your account was inactive."
                        return render(request,'life/patient_login.html',{'error': error})

                if user:
                        if user.is_active:
                                login(request, user)
                                return redirect('/patient/'+username)
                        else:   
                                error= "*Your account was inactive."
                                return render(request,'life/patient_login.html',{'error': error})
                else:
                        error='*Invalid Username and/or password'
                        return render(request,'life/patient_login.html',{'error': error})
        else:   
                error=''
                if(msg==2):
                        error='You are successfully logged out'
                return render(request,'life/patient_login.html',{'error': error})


@login_required(login_url='/login/docto/1r',redirect_field_name=None)
@user_passes_test(lambda user: user.username[0]=='D',login_url='/login/doctor',redirect_field_name=None)
def DoctorDetails(request,doctor_id):
     doctor=get_object_or_404(Doctor,pk=doctor_id)
     appointments=Appointment.objects.all().filter(dname=doctor)    

     return render(request,'life/doctor_details.html',{'doctor':doctor,
                                                           'appointments':appointments                     
                                                        })


@login_required(login_url='/login/patient/1',redirect_field_name=None)
@user_passes_test(lambda user: user.username[0]=='P',login_url='/login/patient',redirect_field_name=None)
def PatientDetails(request,patient_id):
     patient=get_object_or_404(Patient,pk=patient_id)
     appointments=Appointment.objects.all().filter(pname=patient)    
     if request.method=='POST':
                form=Appointment_form(request.POST)
                if form.is_valid():
                                post=form.save(commit=False)
                                obj=Patient.objects.all().filter(pid=request.user.username)
                                post.pname=obj[0]
                                post.save()
                                return redirect('/patient/'+request.user.username)
                                
     form=Appointment_form()   
     return render(request,'life/patient_details.html',{'patient':patient,
                                                           'appointments':appointments,'form':Appointment_form                    
                                                        })



def Logout(request):

    username=request.user.username
    logout(request)
    if(username[0]=='P'):
            utype='patient'
    else:
            utype='doctor'

    return redirect('/login/{}/2'.format(utype))



