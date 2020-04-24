from django.urls import path
from . import views
from survey.views import startapp,  login_view, profile


urlpatterns = [
    path('', startapp, name='index') ,
    path('login', login_view ,name='login' ),
    path('profile', profile, name='profile')
    
]
