from django.urls import path
from .views import PatientView, detail, add_patient

urlpatterns = [
    path('', PatientView.as_view(), name='index'),
    path('<int:patient_id>/details', detail, name="detail"),
    path('add/', add_patient, name="add_patient"),
]

app_name = "mainpage"