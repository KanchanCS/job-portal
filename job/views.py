from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    ApplicantEditForm,
    ApplicantForm,
    ContactForm,
    CreatePostForm,
    LoginForm,
    RegisterForm,
    SheduleForm,
)
from .models import Applicant, JobPost

# Create your views here.


# Home Page Views


# carrier views


def carrier(request):
    recent_jobs = (
        JobPost.objects.all()
        .select_related("company")
        .order_by("-created_date")
    )
    paginator = Paginator(recent_jobs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("job:carrier")
    else:
        form = CreatePostForm()

    context = {"page_obj": page_obj, "form": form}
    return render(request, "carrier.html", context)


# about views


def about(request):
    return render(request, "about.html")


# account views
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("job:home")
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }
    return render(request, "account/register.html", context)


# login views
def login_request(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect("job:home")
    else:
        form = LoginForm()

    context = {"login_form": form}
    return render(request, "account/login.html", context)


# logout views


def logout_request(request):
    logout(request)
    return redirect("job:login")


# contact views


def contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(
                request,
                "Contact request submitted successfully.",
            )
            return redirect("job:home")
        else:
            messages.error(request, "Invalid form submission.")
            messages.error(request, contact.errors)
    else:
        contact = ContactForm()

    context = {"contact": contact}
    return render(request, "contact.html", context)


# applicant views


@login_required(login_url="job:login")
def applicant(request, job_id):
    job_id = JobPost.objects.get(id=job_id)
    apply_list = Applicant.objects.filter(user=request.user).order_by(
        "create_date"
    )[:5]
    user = request.user
    if user is not None:
        if request.method == "POST":
            form = ApplicantForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = user
                data.job_post = job_id
                data.save()

                send_mail(
                    "job_id.job_title",
                    "Your job has been successfully applied.",
                    "kanchan111yadav@gmail.com",
                    [request.user.email],
                    fail_silently=False,
                )
                return redirect("job:home")

        else:
            form = ApplicantForm()
    context = {
        "form": form,
        "job_id": job_id,
        "apply_list": apply_list,
    }
    return render(request, "apply.html", context)


# home pages views


def home(request):
    recent_jobs = (
        JobPost.objects.all()
        .select_related("company")
        .order_by("-created_date")[:5]
    )
    context = {"recent_jobs": recent_jobs}
    return render(request, "index.html", context)


def search_results(request):
    query = request.GET.get("search")
    search_list = JobPost.objects.filter(
        Q(job_title__contains=query) | Q(required_skill__contains=query)
    )
    return render(
        request,
        "search-result.html",
        {
            "search_list": search_list,
        },
    )


# dashboard Views


def recuter(request):
    is_staff = request.user.is_staff
    if is_staff:
        applicant = Applicant.objects.all().order_by("-create_date")
        return render(request, "hr-recuter.html", {"applicant": applicant})
    else:
        return redirect("/")


def delete_applicant(request, id):
    applicant = get_object_or_404(Applicant, id=id)
    applicant.delete()
    return redirect("job:hr-recuter")


def change_status(request, id):
    is_staff = request.user.is_staff
    if is_staff:
        applicant = get_object_or_404(Applicant, id=id)
        if request.method == "POST":
            form = ApplicantEditForm(instance=applicant, data=request.POST)
            if form.is_valid():
                form.save()
                send_mail(
                    "Update Status",
                    f"You are status is {form.cleaned_data['status']} for job {applicant.job_post.job_title}",
                    "kanchan111yadav@gmail.com",
                    [request.user.email],
                    fail_silently=False,
                )
                return redirect("job:hr-recuter")
        else:
            form = ApplicantEditForm(instance=applicant)
        return render(
            request,
            "applicant-edit.html",
            {"form": form, "applicant": applicant},
        )
    else:
        return redirect("job:login")


def shedule(request, id):
    is_staff = request.user.is_staff
    if is_staff:
        job_id = get_object_or_404(JobPost, id=id)
        user = request.user
        if request.method == "POST":
            form = SheduleForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = user
                data.job = job_id
                form.save()
                return redirect("job:hr-recuter")
        else:
            form = SheduleForm()
        return render(request, "shedule.html", {"form": form})
    else:
        return redirect("job:login")
