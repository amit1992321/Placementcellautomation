from django.shortcuts import render
from TpoPanel.forms import SignUpForm, TPO_reg_form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from EmployerPanel.models import Employer, JobPost
from StudentPanel.models import StudentPersonalDetail
from JobApplication.models import JobApplication
# Create your views here.


def tpo_signup(request):
    if request.user.is_authenticated:
        if "tpo_group" in [i.name for i in request.user.groups.all()]:
            return HttpResponseRedirect(reverse('tpo_dash'))
        else:
            return HttpResponseRedirect(reverse('home_page'))
    if request.method == 'POST':
        tpos_reg = SignUpForm(request.POST)
        if tpos_reg.is_valid():
            username = tpos_reg.cleaned_data['username']

           # password = tpos_reg.cleaned_data['TPO_Password']

            # Create new user
            u = User.objects.create(
                username=username,
                first_name=tpos_reg.cleaned_data['first_name'],
                last_name=tpos_reg.cleaned_data['last_name'],
                email=tpos_reg.cleaned_data['email'],
                is_active=True)
            u.set_password(tpos_reg.cleaned_data['password'])
            my_group = Group.objects.get(name='tpo_group')
            my_group.user_set.add(u)
            u.save()
            return HttpResponseRedirect(reverse('tpo_signin'))
    else:
        tpos_reg = SignUpForm()
    return render(request, "tpo_signup.html", {'tpos_reg': tpos_reg})


def tpo_register(request):
    if request.method == 'POST':
        tpo_reg_ = TPO_reg_form(request.POST)
        if tpo_reg_.is_valid():
            tpo_reg_.save()
            return HttpResponseRedirect(reverse('tpo_dash'))
    else:
        tpo_reg_ = TPO_reg_form()
    return render(request, 'tpo_register.html', {})


def tpo_dashboard(request):
    return render(request, "tpo_dashboard.html", {})


def tpo_profile(request):
    return render(request, "tpo_profile.html", {})


def tpo_employer_list(request):
    emp_objs = Employer.objects.all()
    emp_list = []
    for emp_obj in emp_objs:
        emp_list.append(
            {
                'obj': emp_obj,
                'job_post_count': JobPost.objects.filter(employer=emp_obj).count()
            }
        )
    return render(request, 'allemployer.html', {'emp_list': emp_list})


def tpo_student_list(request):
    stu_objs = StudentPersonalDetail.objects.all()
    stu_list1 = []
    for stu_obj in stu_objs:
        stu_list1.append({'obj': stu_obj})
    return render(request, 'allstudent.html', {'stu_list1': stu_list1})


def tpo_job_post_list(request):
    all_job_posts = JobPost.objects.all()
    required_job_post = []
    for job_post in all_job_posts:
        job_application = JobApplication.objects.filter(
            student__user=request.user, jobpost=job_post)
        if(len(job_application) == 0):
            required_job_post.append(job_post)
    return render(request, 'alljobpost.html', {'obj': required_job_post})
