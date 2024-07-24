from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from typing import Any
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"autofocus": True}), required=False)

    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields["username"].required = False

    def clean(self) -> dict[str, Any]:
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if username and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
        elif email and password:
            self.user_cache = User.objects.get(email=email)
            if not self.user_cache.check_password(password):
                self.user_cache = None
        else:
            self.user_cache = None

        if self.user_cache is None:
            raise self.get_invalid_login_error()
        else:
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"autofocus": True}))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    