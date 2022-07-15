from django.http import Http404
from django.views import View
from django.shortcuts import redirect, render
from .forms import PatientForm
from .models import Patient

# Create your views here.

class PatientView(View):

    def get(self,request):
        patient_list = Patient.objects.order_by("last_name")
        context = {
            "patient_list": patient_list,
        }
        return render(request, "mainpage/index.html", context)

def detail(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient is nonexistent")
    context = {
        "patient": patient,
    }
    return render(request, "mainpage/patient_detail.html", context)

def add_patient(request):
    if request.method == "POST":
        patient_form = PatientForm(request.POST, request.FILES)
        if patient_form.is_valid():
            patient_form.save()
            return redirect("mainpage:index")
    else:
        patient_form = PatientForm()
        context = {
            "patient_form": patient_form,
        }
        return render(request, "mainpage/add_patient.html", context)