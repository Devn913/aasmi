from django.urls import path
from . import views

app_name = 'safety'
urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing-page'),
    path('complaints/view/', views.ViewComplaintView.as_view(),
         name='view_complaints'),
    path('complaints/add/', views.AddComplaintView.as_view(), name='add_complaints'),
    path('complaints/all/', views.ShowPanelComplaints.as_view(),
         name='all_complaints'),
    path('complaints/action/<int:pk>', views.TakeActionAgainstComplaint.as_view(),
         name='take_action_complaints'),
    path('complaints/view/<int:pk>', views.ComplaintDetailView.as_view(),
         name='view_complaint'),
    path('complaints/delete/<int:id>',
         views.withdrawComplaint, name='withdraw_complaint'),
    path('report/add/', views.AddVolunteerAction.as_view(),
         name='add_volunteer_action'),
    path('reports/view/', views.ViewVolunteerReports.as_view(),
         name='volunteer_reports'),
    path('reports/all/', views.AllVolunteerReports.as_view(),
         name='all_volunteer_reports'),
]
