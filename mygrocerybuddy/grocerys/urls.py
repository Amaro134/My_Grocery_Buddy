from django.urls import path
from . import views
# Define the URL patterns for the grocerys app
urlpatterns = [
    path('grocery_list/', views.groceryListPage, name='grocery_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
]