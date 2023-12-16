from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from carmart.form.registration import RegistrationForm


def index(req):
    return redirect("/carmart")


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged In Successfully")
                return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def user_logout(request):
    username = request.user.username
    logout(request)
    messages.warning(request, f"Logged Out Successfully")
    return redirect("home")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Your account has been created successfully. Please log in.",
            )
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "signup.html", {"form": form})
