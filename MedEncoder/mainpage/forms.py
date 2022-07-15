from django.forms import ModelForm
from .models import Patient
from django import forms 

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ["last_name", "first_name", "address", "sex", "diagnosis", "last_checkup", "lab_results_date", "lab_results_img"]