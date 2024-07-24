from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from typing import Any
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields["username"].required = False

    def clean(self) -> dict[str, Any]:
        username = self.cleaned_data.get("username")
        email = None
        if "@" in username:
            email = username
            username = None
        password = self.cleaned_data.get("password")
        if username and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
        elif email and password:
            try:
                self.user_cache = User.objects.get(email=email)
                if not self.user_cache.check_password(password):
                    self.user_cache = None
            except User.DoesNotExist:
                self.user_cache = None
        else:
            self.user_cache = None

        if self.user_cache is None:
            raise self.get_invalid_login_error()
        else:
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    
class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    
    def clean_email(self):
        """Reject emails that differ only in case."""

        email = self.cleaned_data.get("email")
        if (
            email
            and self._meta.model.objects.filter(email__iexact=email).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "email": self.instance.unique_error_message(
                            self._meta.model, ["email"]
                        )
                    }
                )
            )
        else:
            return email
    
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {"username": UsernameField, "email": EmailField}