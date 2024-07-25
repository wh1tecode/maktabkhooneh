from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib import messages
from accounts.forms import CustomAuthenticationForm
from django.contrib.sites.models import Site
from django.middleware.csrf import get_token
from accounts.forms import CustomUserCreationForm
from accounts.utils import save_errors
# Create your views here.


def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("website:index")
    if request.POST:
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            messages.add_message(
                request=request, level=messages.SUCCESS, message="user login success"
            )
            login(request, form.user_cache)
            return redirect("website:index")
        save_errors(request, form)
        
    form = CustomAuthenticationForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form},
    )


@login_required
def logout_view(request: HttpRequest):
    logout(request)
    return redirect("website:index")


def signup_view(request: HttpRequest):
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request=request, level=messages.SUCCESS, message="your signup successfully done"
            )
            return redirect("website:index")
        save_errors(request, form)

    return render(request=request, template_name="signup.html")


def forget_password_view(request: HttpRequest):
    current_site = Site.objects.get_current()

    if request.POST:
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            csrf_token = get_token(request)
            form.save(
                subject_template_name="subject_template_name.txt",
                email_template_name="reset_password.html",
                from_email="test@localhost",
                html_email_template_name="reset_password.html",
                extra_email_context={"csrf_token": csrf_token},
            )
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="check your email for reset password",
            )
        save_errors(request, form)

    form = PasswordResetForm()
    return render(
        request=request,
        template_name="forget_password.html",
        context={"form": form, "site_name": current_site.name},
    )
