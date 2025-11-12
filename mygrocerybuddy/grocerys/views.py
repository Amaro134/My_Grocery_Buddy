from django.shortcuts import render
from django.shortcuts import render
from .models import GroceryItem
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# Create your views here.
def groceryListPage(request):
    return render(request, 'grocery_list.html')

#@login_required
def dashboard(request):
#     user = request.user
#     grocery_items = GroceryItem.objects.filter(user=user).order_by('-created_at')

#     # Summary statistics
#     total_entries = grocery_items.count()
#     most_recent_item = grocery_items.first().name if grocery_items.exists() else "No items yet"

#     # Count frequent items
#     frequent_items = (
#         grocery_items.values('name')
#         .annotate(count=Count('name'))
#         .order_by('-count')[:2]
#     )
#     most_frequent = ', '.join([item['name'] for item in frequent_items]) if frequent_items else "None"

#     context = {
#         'user': user,
#         'grocery_items': grocery_items,
#         'total_entries': total_entries,
#         'most_recent_item': most_recent_item,
#         'most_frequent': most_frequent,
#     }

    return render(request, 'dashboard.html')
