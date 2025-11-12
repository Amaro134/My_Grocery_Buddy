from django.urls import path
from . import views
# Define the URL patterns for the main app

urlpatterns = [
    path('', views.landingPage, name='landingpage'), 
    path('home/',  views.homePage, name='homepage'),

]