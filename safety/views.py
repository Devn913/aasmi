from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse, request
from typing import Any

from safety.models import Complaint, VolunteerAction
from .forms import ComplaintForm, ComplaintUpdateForm, VolunteerActionForm
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ComplainantMixin, PanelLoginMixin, VolunteerLoginMixin


class LandingPage(TemplateView):
    """
    Redirect User based on the applied permissions
    """

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            if request.user.is_volunteer:
                return HttpResponseRedirect(reverse('safety:add_volunteer_action'))
            elif request.user.is_complainant:
                return HttpResponseRedirect(reverse('safety:view_complaints'))
            elif request.user.is_panelist:
                return HttpResponseRedirect(reverse('safety:all_complaints'))
        return super().get(request, *args, **kwargs)
    template_name = 'index.html'
    login_url = '/accounts/login/'


# --------------> Complaint Views <-----------------

class AddComplaintView(ComplainantMixin, CreateView):
    # Inherit from CreateView and dispatch function from the ComplainantMixin
    # Dispatch func is the first to get called and decide what request method should be called next
    template_name = "add_complaint.html"
    form_class = ComplaintForm

    # Success URL - After successfull submission of the data, my complaints is loaded up
    def get_success_url(self):
        return reverse('safety:view_complaints')

    def form_valid(self, form):
        # save the instance but don't commit the data to the DB
        # set the complainant to the current logged in user
        # save the updated data
        complaint = form.save(commit=False)
        complaint.complainant = self.request.user
        complaint.save()
        return super().form_valid(form)


class ViewComplaintView(ComplainantMixin, ListView):
    """
    List Complaints under the logged in user
    """
    template_name = 'list_complaints.html'
    context_object_name = 'complaints'

    def get_queryset(self):
        # get all complaints under the logged in user
        complaints = Complaint.objects.filter(
            complainant=self.request.user)
        return complaints


def withdrawComplaint(request, id):
    # delete complaint after receiving id from the url
    Complaint.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse("safety:view_complaints"))


class ComplaintDetailView(DetailView):
    """
    Show Complaint Details
    """
    template_name = "complaint.html"
    model = Complaint
    context_object_name = 'complaint'

# --------------> Panel Section <------------------


class ShowPanelComplaints(PanelLoginMixin, ListView):
    # Inherit from CreateView and dispatch function from the PanelLoginMixin
    # Dispatch func is the first to get called and decide what request method should be called next
    """
    List All Complaints under the logged in user
    """
    template_name = 'show_panel_complaints.html'
    context_object_name = 'complaints'

    def get_queryset(self):
        # get all complaints in the database
        complaints = Complaint.objects.all()
        return complaints


class TakeActionAgainstComplaint(PanelLoginMixin, UpdateView):
    """
    Update Action Against a Complaint
    """
    template_name = "add_action_complaint.html"
    form_class = ComplaintUpdateForm
    model = Complaint

    def get_success_url(self):
        return reverse("safety:all_complaints")


class AllVolunteerReports(PanelLoginMixin, ListView):
    """
    List All Volunteer Reports
    """
    template_name = 'list_all_volunteer_reports.html'
    context_object_name = 'actions'

    def get_queryset(self):
        # get all reports in the database
        actions = VolunteerAction.objects.all()
        return actions

# --------------> Volunteer Section <-----------------


class AddVolunteerAction(VolunteerLoginMixin, CreateView):
    # Inherits VolunteerLoginMixin for authorization and CreateView for Creation of DB
    """
    Logged in User can add Volunteer Report from this view
    """
    template_name = "add_volunteer_action.html"
    form_class = VolunteerActionForm

    # Redirect URL after submission
    def get_success_url(self):
        return reverse('safety:volunteer_reports')

    # Set the volunteer to the logged in user from the action instance
    def form_valid(self, form):
        action = form.save(commit=False)
        action.volunteer = self.request.user
        action.save()
        return super().form_valid(form)


class ViewVolunteerReports(VolunteerLoginMixin, ListView):
    """
    List All Volunteer Reports Made by the logged in User
    """
    template_name = 'list_volunteer.html'
    context_object_name = 'actions'

    def get_queryset(self):
        # get all reports under the logged in user
        actions = VolunteerAction.objects.filter(
            volunteer=self.request.user)
        return actions
