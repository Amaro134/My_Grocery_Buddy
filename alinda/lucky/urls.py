# lucky/urls.py

from django.urls import path
from .views import (
    home,
    CustomLoginView, 
    CustomLogoutView, 
    signup, 
    list_items,     
    add_item,       
    edit_item,      
    delete_item,    
    toggle_complete, 
    clear_completed, 
    clear_all       
)

app_name = 'lucky'

urlpatterns = [
    path('', home, name='home'),
    path('list/', list_items, name='list_items'), 

    # --- Authentication (Fixes NoReverseMatch) ---
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/logout/', CustomLogoutView.as_view(), name='logout'), 
    path('auth/signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # --- Item Management ---
    path('add/', add_item, name='add_item'),
    path('toggle/<int:item_id>/', toggle_complete, name='toggle_complete'),
    path('edit/<int:item_id>/', edit_item, name='edit_item'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    
    # --- Bulk Actions ---
    path('clear-completed/', clear_completed, name='clear_completed'),
    path('clear-all/', clear_all, name='clear_all'),
]