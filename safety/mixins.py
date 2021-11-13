
from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


class ComplainantMixin(AccessMixin):
    # Verify the current user is authenticated and is a complaintant
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_complainant:
            return redirect("safety:landing-page")
        return super().dispatch(request, *args, **kwargs)


class PanelLoginMixin(AccessMixin):
    # Verify the current user is authenticated and is a faculty
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_panelist:
            return redirect("safety:landing-page")
        return super().dispatch(request, *args, **kwargs)


class VolunteerLoginMixin(AccessMixin):
    # Verify the current user is authenticated and is a student
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_volunteer:
            return redirect("safety:landing-page")
        return super().dispatch(request, *args, **kwargs)
