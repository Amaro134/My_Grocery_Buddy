from django.urls import path
from . import views
# Define the URL patterns for the main app

urlpatterns = [
    path('home/',  views.homePage, name='home'),
    path('', views.landingPage, name='landingpage'), 
    path('profile', views.profilePage, name='profile')
    

]