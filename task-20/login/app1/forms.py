from django import forms
from django.forms import models
from .models import employee
from django import forms
from django.forms import models

class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ["img","bio","fname","mname","lname","number","dob","email","country","state","dist","edu","college","year","mark","role","duration","sal"]
