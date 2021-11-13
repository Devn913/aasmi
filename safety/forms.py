from django import forms
from django.db.models import fields
from .models import Complaint, VolunteerAction
from django.forms import DateInput


class ComplaintForm(forms.ModelForm):
    # Model Form Takes in the DB Model
    class Meta:
        model = Complaint
        # field to exclude
        exclude = ('complainant', 'action',
                   'action_description', 'action_report')
        # widgets to use
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }


class ComplaintUpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('action', 'action_description', 'action_report')


class VolunteerActionForm(forms.ModelForm):
    class Meta:
        model = VolunteerAction
        fields = ('name', 'date', 'report', 'action')

        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }
