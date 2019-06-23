from django.contrib import admin

# Register your models here.

from EmployerPanel.models import Employer, JobPost, CompanyDetails

admin.site.register(Employer)
admin.site.register(JobPost)
admin.site.register(CompanyDetails)
