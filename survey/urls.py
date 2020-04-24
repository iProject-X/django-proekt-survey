from django.urls import path
from . import views
from survey.views import startapp,  login_view, profile, login, logout



urlpatterns = [
    path('', startapp, name='startapp') ,
    path('login', login_view ,name='login' ),
    path('profile', profile, name='profile'),
    path('login', login, name='login'),
    path('logout', logout, name='logout')
    
]
