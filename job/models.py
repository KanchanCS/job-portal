from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    company_url = models.URLField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class JobPost(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=2)
    job_title = models.CharField(max_length=65)
    job_detail = models.TextField(blank=True)
    job_image = models.ImageField(upload_to=f"{company.name}/job_detail/")
    expercince = models.CharField(max_length=50, null=True)
    vacancy = models.IntegerField(null=True)
    job_type = models.CharField(max_length=50)
    required_skill = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return self.job_title


class Applicant(models.Model):
    STATUS = (
        ("Pending", "pending"),
        ("Rejected", "rejected"),
        ("Approved", "approved"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resume/")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS, default=STATUS[0][0]
    )
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username


class Shedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    link = models.URLField(max_length=100)
    details = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
