from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('age', 'specialite', 'language')

