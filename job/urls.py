from django.urls import path

from . import views

app_name = "job"
urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    path("search/", views.search_results, name="search-results"),
    # carrier page
    path("carrier/", views.carrier, name="carrier"),
    # about page
    path("about/", views.about, name="about"),
    # contact page
    path("contact/", views.contact, name="contact"),
    # register page
    path("register/", views.register_user, name="register"),
    # post-details

    path("apply/<int:job_id>", views.applicant, name="apply"),
    # login page
    path("login/", views.login_request, name="login"),
    # logout page
    path("logout/", views.logout_request, name="logout"),
    # HR_recuter page
    path("dash/", views.recuter, name="hr-recuter"),
    path('dash/delete/<int:id>', views.delete_applicant, name="delete"),

    # change status
    path("dash/change/status/<int:id>", views.change_status, name="change-status"),

    path("shedule/<int:id>", views.shedule, name="shedule"),
]
