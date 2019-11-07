from django.contrib import admin
from .models import Doctor,Patient,Department,Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(Appointment)