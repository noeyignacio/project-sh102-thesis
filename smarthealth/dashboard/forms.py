from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from patients.models import Patient

class CreatePatientForm(UserCreationForm)
    class Meta:
        model = Patient
        fields = [
            ''
        ]