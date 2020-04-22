from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import *

class ExtendedUserCreationForm(UserChangeForm):
    first_name = forms.CharField(max_length= 100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'email')
    def save(self, commit=True):
        user = super().save(commit==False)

        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class UserProfil(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('age', 'specialite', 'language')
   
   
   
  