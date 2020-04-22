from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


#def startapp(request):
#    if request.method == 'POST':
#        fullname = request.POST['fullname']
#        age = request.POST['age']
#        email = request.POST['email']
#        specialite = request.POST['specialite']
#        language = request.POST['language']
#        vibor_test = Vibor_test.objects.all() 
#        vb = [vibor_test]  
#        user = User.objects.create(fullname=fullname, age=age, email=email, 
#                                specialite=specialite, language=language)
#        user.save()
#        print('lalalal')
#        return redirect('/admin',{'vb': vibor_test})
#    else:
#        return render(request, 'index.html')

#def startapp(request): 
#    context ={}
#    form = User(request.POST) 
#    if form.is_valid():
#        form.save()
#        return test(request)
#        
#    else:
#        return render(request, "index.html", context ) 
#  
#def test(request):
#        #survey = Otvet.objects.all().order_by('?')[:1]
#        return render(request, 'test.html', {"survey":survey})        
#
#def next(request):
#    pass


def startapp(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profil_form = UserProfil(request.POST)

        if form.is_valid() and profil_form.is_valid():
            user = form.save()

            profile = profil_form.save(commit=False)
            profile.user    

            profile.save()

            first_name = form.cleaned_data.get('first_name')
            login(request, user)

            return redirect('startapp')
    else:
        form = ExtendedUserCreationForm()
        profil_form = UserProfil()
    context = {'form': form, 'profil_form': profil_form}
    return render(request, 'home.html', context)