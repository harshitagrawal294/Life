import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Department(models.Model):
    name= models.CharField(max_length=200)
    hod= models.CharField(max_length=200)
    number_of_doc= models.IntegerField()
    picture=models.ImageField(upload_to='department/',null=True)
    picture_big=models.ImageField(upload_to='department/',null=True)
    desc= models.CharField(max_length=300, null=True)



    def __str__(self):
        return self.name

class Doctor(models.Model):
    name= models.CharField(max_length=200)
    eid= models.CharField(max_length=200,primary_key=True)
    dept= models.ForeignKey(Department,on_delete=models.CASCADE)
    picture= models.ImageField(upload_to="doctors/",null=True)
    designation= models.CharField(max_length=200)
    password = models.CharField(max_length=64,default='xyz')


    def __str__(self):
        return self.name


class Patient(models.Model):
    name= models.CharField(max_length=200)
    pid= models.CharField(max_length=200,primary_key=True)
    age= models.IntegerField()
    picture= models.ImageField(upload_to="doctors/",null=True)
    password = models.CharField(max_length=50,default='xyz')
    past_record=models.TextField(max_length=300,default='')


    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    dname=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pname= models.ForeignKey(Patient, on_delete=models.CASCADE)
    dtime = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return str(self.dname)+' '+ str(self.pname)
    

    
    
