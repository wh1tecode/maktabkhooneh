from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get('PATH_INFO', "")
        if settings.MY_MAINTENANCE_MODE:
            if settings.MY_MAINTENANCE_MODE and path != reverse("maintenance"):
                response = redirect(reverse("maintenance"))
                return response

        response = self.get_response(request)

        return response