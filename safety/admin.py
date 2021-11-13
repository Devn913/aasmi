from django.contrib import admin
from .models import Complaint, User, VolunteerAction
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
import csv


def download_complainant_csv(modeladmin, request, queryset):
    f = open('complaints.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(["ID", "Subject", "Date", "Proof", "Description", "Action", "Action Description", "Action Report",
                    "Complainant Name", "Complainant Email", "Complainant Phone", "Complainant Type", "Complainant Department"])
    for s in queryset:
        writer.writerow([s.id, s.subject, s.date, s.proof.url, s.description, s.action, s.action_description, s.action_report.url, s.complainant.first_name +
                        ' ' + s.complainant.last_name, s.complainant.email, s.complainant.phone_number, s.complainant.type, s.complainant.department])


def download_volunteer_csv(modeladmin, request, queryset):
    f = open('volunteer.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Date", "Report",
                    "Volunteer Event Type", "Volunteer Name", "Volunteer Email", "Volunteer Phone", "Volunteer Type", "Volunteer Department"])
    for s in queryset:
        writer.writerow([s.id, s.name, s.date, s.report.url, s.action, s.volunteer.first_name +
                        ' ' + s.volunteer.last_name, s.volunteer.email, s.volunteer.phone_number, s.volunteer.type, s.volunteer.department])


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('User Information', {
            'fields': ('username', 'password')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'department', 'type')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_volunteer', 'is_complainant', 'is_panelist'),
        }),
    )

    add_fieldsets = (
        ('User Information', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }), ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'department', 'type')
        }),
        ('User Type', {
            'fields': ('is_volunteer', 'is_complainant', 'is_panelist'),
        }),)


@admin.register(Complaint)
class CustomComplaintAdmin(admin.ModelAdmin):
    list_display = ('complainant', 'date', 'action')
    actions = [download_complainant_csv]

    fieldsets = (
        ('Compaint Information', {
            'fields': ('subject', 'date', 'description', 'proof')
        }),
        ('Action Information', {
            'fields': ('action', 'action_description', 'action_report')
        }),
        ('Complainant Information', {
            'classes': ('collapse',),
            'fields': ('complainant',),
        }),
    )

    add_fieldsets = (
        ('User Information', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }), ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'department', 'type')
        }),
        ('User Type', {
            'fields': ('is_volunteer', 'is_complainant', 'is_panelist'),
        }),)


@admin.register(VolunteerAction)
class CustomVolunteerAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'date', 'name')
    actions = [download_volunteer_csv]
    fieldsets = (
        ('Compaint Information', {
            'fields': ('name', 'date', 'report', 'action')
        }),
        ('Volunteer Information', {
            'classes': ('collapse',),
            'fields': ('volunteer',),
        }),
    )

    add_fieldsets = (
        ('User Information', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }), ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'department', 'type')
        }),
        ('User Type', {
            'fields': ('is_volunteer', 'is_complainant', 'is_panelist'),
        }),)
