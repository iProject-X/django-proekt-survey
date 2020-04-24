from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfil
from django.contrib.auth.forms import AuthenticationForm




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

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'username ne korrektno'
    context = {'username': username}
    return render(request, 'index.html', context)





def startapp(request):
    
    if request.method == 'POST':

        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfil(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user   

            profile.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            

            return redirect('login')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfil()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registeration.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return profile(request)

    else:
        form = AuthenticationForm()
    context = { 'form': form}
    return render(request, 'login.html', context)


@login_required
def profile(request):

    return render(request, 'home.html')

def logout(request):
    return render(request, '/')