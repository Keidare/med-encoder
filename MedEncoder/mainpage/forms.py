from django.forms import ModelForm
from .models import Patient
from django import forms 

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ["last_name", "first_name", "address", "sex", "diagnosis", "last_checkup", "lab_results_date", "lab_results_img"]
        widgets = {
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'sex': forms.TextInput(attrs={'class':'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'last_checkup': forms.DateInput(attrs={'class':'form-control'}),
            'lab_results_date': forms.DateInput(attrs={'class':'form-control'}),
            'lab_results_img': forms.FileInput(attrs={'class':'form-control'})
        }