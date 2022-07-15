from django.db import models
# Create your models here.

class Patient(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    diagnosis = models.TextField()
    last_checkup = models.DateField()
    sex = models.CharField(max_length=1)
    lab_results_date = models.DateField()
    address = models.CharField(max_length=100)
    lab_results_img = models.ImageField(upload_to='mainpage/images')
