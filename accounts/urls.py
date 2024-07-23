from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("signup", signup_view, name="signup"),
    path("forget_password", forget_password_view, name="forget_password"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("accounts:login"),
            template_name="password_reset_confirm.html",
            post_reset_login=True,
        ),
        name="password_reset_confirm",
    ),
]
