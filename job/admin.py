from django.contrib import admin

from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name", "email"]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date"]
    search_fields = ["name", "create_date"]
    list_filter = ['name', "create_date"]


class JobPostAdmin(admin.ModelAdmin):
    list_display = ["job_title", "job_type", "company"]
    search_fields = ["job_type", "job_title", "created_date"]
    list_filter = ['company', "created_date"]


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['user',  'job_post', 'create_date']
    search_fields = ['user', 'company', 'job_post']
    list_filter = ['user', "create_date"]

class SheduleAdmin(admin.ModelAdmin):
    list_display = ['user',  'job', 'create_date']
    list_filter = ['user', "create_date"]

#admin.site.register(Contact, Interview_shaduleAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Shedule, SheduleAdmin)