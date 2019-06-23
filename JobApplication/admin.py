from django.contrib import admin

# Register your models here.
from JobApplication.models import JobApplication, JobApplicationHistory

admin.site.register(JobApplication)
admin.site.register(JobApplicationHistory)
