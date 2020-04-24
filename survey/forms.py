from django import forms
from .models import Profil, Otvet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class ExtendedUserCreationForm(UserCreationForm):

    
    email = forms.EmailField(required=True)
   
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2'  )

    def save(self, commit=True):
        user = super().save(commit==False)
        user.email = self.cleaned_data['email']
       

        if commit:
            user.save()
        return user

class UserProfil(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('fullname', 'age', 'specialite', 'language')
   


   
  