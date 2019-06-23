from django import forms
import datetime
from . import models
from django.forms import formset_factory


class EmployerForm(forms.ModelForm):
    class Meta:
        model = models.Employer
        fields = ['user', 'mobile', 'alternate_mobile', 'company_details']


class JobPostForm(forms.ModelForm):
    class Meta:
        model = models.JobPost
        fields = ['employer',
                  'job_Profile',
                  'job_vacancy',
                  'job_description',
                  'job_ctc',
                  'interview_date',
                  ]


class CompanyDetailForm(forms.ModelForm):
    company = forms.CharField(max_length=120, label="Username", widget=forms.Select(
        attrs={
            'placeholder': 'Username'
        },
        choices=models.CompanyDetails.objects.all().values_list('id', 'company_name')
    ))

    class Meta:
        model = models.CompanyDetails
        fields = ['industry_type',
                  'company_name',
                  'company_address',
                  'registration_no',
                  'company'
                  ]


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=120, label="Username", widget=forms.TextInput(
        attrs={
            'placeholder': 'Username'
        }))
    first_name = forms.CharField(max_length=200, label="First's Name",
                                 widget=forms.TextInput(
                                     attrs={
                                         'placeholder': 'First Name'
                                     }))
    last_name = forms.CharField(max_length=200)
    mobile = forms.CharField(max_length=10)
    alternate_mobile = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=200, required=False)
    password = forms.CharField(max_length=200)
    repassword = forms.CharField(max_length=200)

    def clean(self):
        # import pdb; pdb.set_trace()
        if self.cleaned_data['password'] != self.cleaned_data['repassword']:
            raise forms.ValidationError(('Password mismatch'), code='invalid')
