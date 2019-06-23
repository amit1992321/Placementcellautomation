from django.shortcuts import render
from JobApplication.forms import StuJobPostApply
from django.http import HttpResponseRedirect
from django.urls import reverse
from JobApplication.models import JobApplication
from StudentPanel.models import StudentJobApplicationDetail
from EmployerPanel.models import JobPost
# Create your views here.


def job_post_apply(request, job_post_id):
    current_user = request.user
    obj = StudentJobApplicationDetail.objects.get(studentpersonaldetail__user=current_user)
    changed_data = {}
    changed_data['application_status'] = 'Inprocess'
    changed_data['jobpost'] = JobPost.objects.get(id=job_post_id)
    if request.method == 'POST':
        changed_data['skills'] = request.POST.get('skills')
        changed_data['achievement'] = request.POST.get('achievement')
        changed_data['resume'] = request.POST.get('resume')
        import ipdb; ipdb.set_trace()
        stu_reg_pro = StuJobPostApply(data=changed_data)
        if stu_reg_pro.is_valid():
            stu_reg_pro.save()
            return HttpResponseRedirect(reverse('stu_dash'))
    else:
        changed_data = {}
        changed_data['skills'] = obj.skills
        changed_data['achievement'] = obj.achievement
        changed_data['resume'] = obj.resume.url
        # import ipdb; ipdb.set_trace()
        stu_reg_pro = StuJobPostApply(data=changed_data)
    return render(request, 'stu_job_application.html', {'stu_reg_pro': stu_reg_pro, 'obj': obj, 'job_id': job_post_id})


def post_job_apply(request):
    return render(request, 'stu_job_application.html', {'success': True})
