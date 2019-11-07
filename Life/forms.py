from django import forms
from .models import Doctor,Department,Patient
class PostForm_Doctor(forms.ModelForm):
        class Meta:
                model=Doctor
                dept= forms.ModelChoiceField(queryset= Department.objects.all(),  to_field_name="name")
                fields=['name','dept','designation','picture','password',]
                labels={
                    'dept':'Department'
                }
                widgets = {
                    'name': forms.TextInput(attrs={'placeholder': '*Enter Fullname'}),
                    'designation': forms.TextInput(attrs={'placeholder': '*Enter your designation as specified by the hospital'}),
                    'password': forms.PasswordInput(attrs={'placeholder': 'Use a strong password', 'size':40}),
                }

class PostForm_Patient(forms.ModelForm):
        class Meta:
                model=Patient
                fields=['name','age','past_record','password','picture']
                widgets = {
                    'name': forms.TextInput(attrs={'placeholder': '*Enter Fullname'}),
                    'password': forms.PasswordInput(attrs={'placeholder': 'Use a strong password', 'size':40}),
                }