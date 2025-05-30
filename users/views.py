"""Views for Registration, Login, and Logout"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from .forms import UserUpdateForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash password
            user.save()
            return redirect("users:login")
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = get_user_model().objects.get(username=username) # get user by username
                user = authenticate(request, username=username, password=password) # authenticate
                if user is not None:
                    login(request, user)
                    return redirect("job_list")
                else:
                    form.add_error('password', "Incorrect password.") # add error to password field.
            except ObjectDoesNotExist:
                form.add_error(None, "Invalid username or password.") # username not found.
        else:
            form.add_error(None, "Invalid username or password.") # form is invalid.

    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("users:login")

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        # profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid():
            user_form.save()
            return redirect('users:profile')

    else:
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'user_form': user_form})
