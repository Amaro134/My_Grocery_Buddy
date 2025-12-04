from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Sum
from django.contrib import messages

from .forms import TaskForm
from .models import Task, CATEGORY_CHOICES


def homePage(request):
    if request.user.is_authenticated:
        return redirect('grocery:list_items')
    return redirect('users:login')



@login_required
def grocery_list(request):
    filter_type = request.GET.get('filter', 'all')
    user = request.user

    base_query = Task.objects.filter(user=user)

    if filter_type == 'completed':
        items = base_query.filter(complete=True).order_by('category', 'title')
    elif filter_type == 'active':
        items = base_query.filter(complete=False).order_by('category', 'title')
    else:
        items = base_query.order_by('category', 'title')

    all_items_for_modal = base_query.order_by('title')

    total_count = all_items_for_modal.count()
    completed_count = all_items_for_modal.filter(complete=True).count()
    remaining_count = total_count - completed_count

    total_price = all_items_for_modal.aggregate(Sum('price'))['price__sum'] or 0
    remaining_price = all_items_for_modal.filter(complete=False).aggregate(Sum('price'))['price__sum'] or 0

    grouped_items = {}
    for category_code, category_name in CATEGORY_CHOICES:
        category_items = items.filter(category=category_code)
        if category_items.exists():
            grouped_items[category_name] = category_items

    if not grouped_items and items.exists():
        grouped_items['All Items'] = items

    context = {
        'form': TaskForm(),
        'grouped_items': grouped_items,
        'all_items': all_items_for_modal,
        'total_count': total_count,
        'completed_count': completed_count,
        'remaining_count': remaining_count,
        'total_price': total_price,
        'remaining_price': remaining_price,
        'filter': filter_type,
        'categories': CATEGORY_CHOICES,
    }

    return render(request, 'grocery_list.html', context)


@login_required
def add_item(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            messages.success(request, f'"{new_task.title}" added successfully!')
            return redirect('grocery:list_items')

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{field.title()}: {error}')

    return redirect('grocery:list_items')


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Task, pk=item_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{item.title}" updated successfully!')
            return redirect('grocery:list_items')

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{field.title()}: {error}')

    return redirect('grocery:list_items')


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Task, pk=item_id, user=request.user)
    item_title = item.title
    item.delete()
    messages.success(request, f'"{item_title}" deleted successfully!')
    return redirect('grocery:list_items')


@login_required
def toggle_complete(request, item_id):
    item = get_object_or_404(Task, pk=item_id, user=request.user)
    item.complete = not item.complete
    item.save()
    return redirect('grocery:list_items')


@login_required
def clear_completed(request):
    count = Task.objects.filter(user=request.user, complete=True).count()
    Task.objects.filter(user=request.user, complete=True).delete()
    messages.success(request, f'{count} completed item(s) cleared!')
    return redirect('grocery:list_items')


@login_required
def clear_all(request):
    count = Task.objects.filter(user=request.user).count()
    Task.objects.filter(user=request.user).delete()
    messages.success(request, f'All {count} item(s) cleared!')
    return redirect('grocery:list_items')


def dashboard(request):
    return render(request, 'dashboard.html')
