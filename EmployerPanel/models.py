from django.db import models
from django.contrib.auth.models import User
from TpoPanel.models import TpoDetails
# Create your models here.


class CompanyDetails(models.Model):
    INDUSTRY_TYPE = (
        ('NONE', 'None'),
        ('IT', 'IT'),
        ('BPO', 'BPO'),
        ('MANUFACTURING', 'Manufacturing'),
        ('MEDIA', 'Media'),
        ('FINANCE', 'Finance'),
        ('MEDICAL', 'Medical'),
        ('CONSTRUCTION', 'Construction'),
        ('TELECOMMUNICATION', 'Telecommunication')
    )

    industry_type = models.CharField(max_length=120, choices=INDUSTRY_TYPE)
    company_name = models.CharField(max_length=120)
    company_address = models.CharField(max_length=120)
    registration_no = models.CharField(max_length=12)

    def __str__(self):
        return self.company_name


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    alternate_mobile = models.CharField(max_length=20)
    company_details = models.ForeignKey(
        CompanyDetails, on_delete=models.CASCADE, null=True)
    is_authorise = models.BooleanField(default=False, null=True)



class JobPost(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    job_Profile = models.CharField(max_length=20)
    job_vacancy = models.CharField(max_length=5)
    job_description = models.TextField()
    job_ctc = models.CharField(max_length=5)
    interview_date = models.DateTimeField()
    register_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False, null=True)
    is_authrise = models.BooleanField(default=False, null=True)
    authorise_by = models.ForeignKey(
        TpoDetails, on_delete=models.CASCADE,null=True)
    last_update = models.DateTimeField(auto_now_add=True)
