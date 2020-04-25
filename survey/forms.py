from django import forms
from survey.models import Profil, Otvet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField





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
   


   
class OtvetForm(forms.ModelForm):
    class Meta:
        model = Otvet
        fields = ('answer','user','stimul')
        user = forms.ModelChoiceField(queryset=Profil.objects.all())
        stimul = forms.ModelChoiceField(queryset=Otvet.objects.all())