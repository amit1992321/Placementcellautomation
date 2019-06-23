from django.contrib import admin

# Register your models here.
from StudentPanel.models import StudentPersonalDetail, StudentEducationalQualifications
from StudentPanel.models import StudentJobApplicationDetail

admin.site.register(StudentPersonalDetail)
admin.site.register(StudentEducationalQualifications)
admin.site.register(StudentJobApplicationDetail)
