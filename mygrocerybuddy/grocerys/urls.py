from django.urls import path
from . import views


urlpatterns = [
    path('', views.grocery_list, name='list_items'),  # main grocery list
    path('grocery_list/', views.grocery_list, name='grocery_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('add_item/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('toggle/<int:item_id>/', views.toggle_complete, name='toggle_complete'),

    path('clear-completed/', views.clear_completed, name='clear_completed'),
    path('clear-all/', views.clear_all, name='clear_all'),
]
