from django.db import models
from EmployerPanel.models import JobPost, Employer
from StudentPanel.models import StudentPersonalDetail
# Create your models here.


class JobApplication(models.Model):
    APPLICATION_STATUS = (
        ('SELECTED', 'Selected'),
        ('REJECTED', 'Rejected'),
        ('INPROCESS', 'Inprocess'),
        ('INTERVIEW SCHEDULED', 'Interview Scheduled'),
        ('ONHOLD', 'Onhold'),
    )
    application_status = models.CharField(
        max_length=20, choices=APPLICATION_STATUS)
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    skills = models.CharField(max_length=121)
    achievement = models.CharField(max_length=12)
    resume = models.FileField(null=True, upload_to='resume_job_application')
    application_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(
        StudentPersonalDetail, on_delete=models.CASCADE, null=True)


class JobApplicationHistory(models.Model):
    changes_by = models.ForeignKey(Employer, on_delete=models.CASCADE)
    changes_on = models.DateTimeField()
    comment = models.CharField(max_length=120)


'''
Story -
1. When student signed in and go to his dashboard, he can see the list of Job Post.
On each job Post, there is button called 'APPLY'

On clicking on 'APPLY' - redirects to the Job Application Form.
This for Contains the similar field of StudentJobApplicationDetail

Job Application - skills , achievement and resume, application date,
application status (Selected, rejected, inprocess, interview scheduled, onhold)

Job Application History -
- Forign key - Job Application
- Changes by - FK - Employeer
- Changes on - Date
- Comment - Char

'''
