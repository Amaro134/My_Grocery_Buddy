from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User


User = get_user_model()

# -------------------- LOGIN --------------------
def loginPage(request):
    context = {"email_error": "", "password_error": "", "email_value": ""}

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        context["email_value"] = email  # Pass this to template

        if not email:
            context["email_error"] = "Email is required."
        if not password:
            context["password_error"] = "Password is required."

        if context["email_error"] or context["password_error"]:
            return render(request, "login.html", context)

        # Adjust depending on your User model
        users = authenticate(request, username=email, password=password)

        if users is None:
            context["password_error"] = "Invalid email or password."
            return render(request, "login.html", context)

        login(request, users)
        return redirect("main:home")

    return render(request, "login.html", context)

   

# signup

def registerPage(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        field_errors = {}

        # Field validation
        if not fullname:
            field_errors["fullname_error"] = "Full name is required."
        if not email:
            field_errors["email_error"] = "Email is required."
        if not password:
            field_errors["password_error"] = "Password is required."
        if not confirm_password:
            field_errors["confirm_password_error"] = "Confirm your password."
        if password and confirm_password and password != confirm_password:
            field_errors["confirm_password_error"] = "Passwords do not match."
        if email and User.objects.filter(email=email).exists():
            field_errors["email_error"] = "Email is already registered."

        # If there are validation errors
        if field_errors:
            request.session["form_errors"] = field_errors
            # Save the previously entered values too (optional)
            request.session["form_values"] = {"fullname": fullname, "email": email}
            return redirect("users:register")

        # Success: create user
        try:
            user = User.objects.create_user(
                email=email,
                password=password,
                full_name=fullname
            )
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("users:login")
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect("users:register")

    # GET request → show form and errors if available
    context = request.session.pop("form_errors", {})
    # Include previous values in the form
    context.update(request.session.pop("form_values", {}))
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect("users:login")
