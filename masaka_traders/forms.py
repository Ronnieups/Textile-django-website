from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','mobile_no','first_name','last_name','location','alternative_mobile_no','broker_mobile_no')