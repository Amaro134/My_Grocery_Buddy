from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm



# Create your views here.
def landingPage(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'home.html')

def profilePage(request):
    return render (request, 'profile.html')


@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("main:home")
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, "main/profile_modal_form.html", {"form": form})


