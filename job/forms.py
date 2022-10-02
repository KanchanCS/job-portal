from dataclasses import fields

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Applicant, Contact, JobPost, Shedule


class DateInput(forms.DateInput):
    input_type = "date"


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    required_css_class = "required"

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "subject",
            "content",
            "created_on",
        ]
        widgets = {"created_on": DateInput()}

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = [
            "resume",
            "github",
            "linkedin",
        ]

    def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class ApplicantEditForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ["status"]

    def __init__(self, *args, **kwargs):
        super(ApplicantEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class SheduleForm(ModelForm):
    class Meta:
        model = Shedule
        fields = [
            "link",
            "details",
        ]

    def __init__(self, *args, **kwargs):
        super(SheduleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class CreatePostForm(ModelForm):
    class Meta:
        model = JobPost
        fields = [
            "job_title",
            "job_detail",
            "job_image",
            "expercince",
            "vacancy",
            "job_type",
            "required_skill",
            "end_date",
        ]
        text_field = forms.Textarea(attrs={"rows": 2, "cols": 30})
        widgets = {
            "end_date": DateInput(),
            "job_detail": text_field,
            "required_skill": text_field,
        }

    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
