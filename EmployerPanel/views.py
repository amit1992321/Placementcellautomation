from django.shortcuts import render
import datetime
from EmployerPanel.forms import SignUpForm, EmployerForm
from EmployerPanel.forms import JobPostForm, CompanyDetailForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from EmployerPanel.models import Employer, JobPost, CompanyDetails
from JobApplication.models import JobApplication
# Create your views here.
from django.forms import formset_factory


def employer_signup(request, user_detail=None, employee=None):
    error = ''
    if request.user.is_authenticated:
        if "employer" in [i.name for i in request.user.groups.all()]:
            return HttpResponseRedirect(reverse('emp_dash'))
        else:
            return HttpResponseRedirect(reverse('home_page'))
    else:
        if request.method == 'POST':
            emp_signup = SignUpForm(request.POST)
            context = {
                'error': error,
                'emp_signup': emp_signup,
            }
            if emp_signup.is_valid():
                username = emp_signup.cleaned_data['username']
                # password = emp_reg.cleaned_data['TPO_Password']
                # Create new user
                u = User.objects.create(
                    username=username,
                    first_name=emp_signup.cleaned_data['first_name'],
                    last_name=emp_signup.cleaned_data['last_name'],
                    email=emp_signup.cleaned_data['email'],
                    is_active=True)
                u.set_password(emp_signup.cleaned_data['password'])
                my_group = Group.objects.get(name='employer')
                my_group.user_set.add(u)
                u.save()
                Employer.objects.create(
                    user=u,
                    mobile=emp_signup.cleaned_data['mobile'],
                    alternate_mobile=emp_signup.cleaned_data['alternate_mobile']
                )
                return HttpResponseRedirect(reverse('signin'))
        else:
            emp_signup = SignUpForm()
            context = {
                'error': error,
                'emp_signup': emp_signup,
            }
        return render(request, "emp_signup.html", context,)


def emp_dashboard(request):
    if not (request.user.is_authenticated and "employer" in
            [
                i.name for i in request.user.groups.all()
            ]):
        return HttpResponseRedirect(reverse('signin'))
    else:
        emp_obj = Employer.objects.filter(user=request.user)
        is_comp_obj = False
        is_emp_obj = len(emp_obj)
        if is_emp_obj:
            is_comp_obj = emp_obj[0].company_details
        return render(request, "emp_dashboard.html", {'is_emp_obj': is_emp_obj, 'is_comp_obj': is_comp_obj})


def emp_profile(request):
    error = ''
    # user_obimport ipdb; ipdb.set_trace()j = User.objects.get(id=request.user)
    try:
        emp_obj = Employer.objects.get(user=request.user)
        comp_obj = emp_obj.company_details
        job_app = JobApplication.objects.filter(application_status="INPROCESS")
        job_app_count = len(job_app)

    except:
        return HttpResponseRedirect(reverse('emp_create_pro'))
    return render(request, 'emp_profile.html', {'emp_obj': emp_obj, "comp_obj": comp_obj, 'error':error})


def emp_stu_list(request):
    obj = JobPost.objects.all()
    return render(request, 'emp_stu_list.html', {'stu_list': obj})


def emp_newjobpost(request):
    error = ''
    if request.method == "POST":
        emp_job = JobPostForm(request.POST)
        import ipdb; ipdb.set_trace()
        context = {
            'emp_job': emp_job,
            'errors': error,
        }
        if emp_job.is_valid():
            emp_job.save()
            return HttpResponseRedirect(reverse('emp_dash'))
    else:
        emp_job = JobPostForm()
        context = {
            'emp_job': emp_job,
            'errors': error
        }
    return render(request, 'emp_job_post.html', context)


def emp_create_pro(request):
    error = ''
    if request.method == "POST":
        emp_pro = EmployerForm(request.POST)
        context = {
            'emp_pro': emp_pro,
            'errors': error
        }
        if emp_pro.is_valid():
            emp_pro.save()
            return HttpResponseRedirect(reverse('emp_dash'))
    else:
        emp_pro = EmployerForm()
        context = {
            'emp_pro': emp_pro,
            'errors': error
        }
    return render(request, 'emp_pro.html', context)


def stu_app_review(request):
    app_request = JobApplication.objects.filter(application_status='INPROCESS')
    # job_post_req = []
    # for job_posts in app_request:
    #   job_application = JobApplication.objects.filter(
    #       student__user=request.user, jobpost=job_posts)
    #  if(len(job_application) == 0):
    #      job_post_req.append(job_posts)
    return render(request, 'emp_app_review.html', {'job_post_req': app_request})


def stu_app(request):
    obj = JobApplication.objects.filter(application_status='INPROCESS')
    return render(request, 'stu_app_sumery.html', {'obj': obj})


def job_post(request):
    obj = JobPost.objects.all()
    return render(request, 'job_post_summary.html', {'stu_list': obj})


def emp_company_details(request):
    emp_com = CompanyDetails.objects.all()
    emp_emp = Employer.objects.all()
    context = {
        'emp_com': emp_com,
        'emp_emp': emp_emp
    }
    return render(request, 'emp_company_detail.html', context)


def emp_reg_info(request):
    error = ''
    if request.method == 'POST':
        emp_signup = SignUpForm(request.POST)
        context = {
            'error': error,
            'emp_signup': emp_signup,
        }
        if emp_signup.is_valid():
            # username = emp_signup.cleaned_data['username']
            # # password = emp_reg.cleaned_data['TPO_Password']
            # # Create new user
            # u = User.objects.create(
            #     username=username,
            #     first_name=emp_signup.cleaned_data['first_name'],
            #     last_name=emp_signup.cleaned_data['last_name'],
            #     email=emp_signup.cleaned_data['email'],
            #     is_active=True)
            # u.set_password(emp_signup.cleaned_data['password'])
            # my_group = Group.objects.get(name='employer')
            # my_group.user_set.add(u)
            # u.save()
            # Employer.objects.create(user=u, 
            #     mobile=emp_signup.cleaned_data['mobile'],
            #     alternate_mobile=emp_signup.cleaned_data['alternate_mobile']
            #     )
            return render(request, 'emp_signup.html', {'emp_signup': context})
            # return HttpResponseRedirect(reverse('signin'))
    else:
        bound_values = {
            'username': "sdsds",
            'first_name': "sdsdsd",
            'last_name': "sdsdd",
            'mobile': '343434',
            'alternate_mobile': '234234',
            'email': '23423',
            'password': '3234234',
            'repassword': '2324324',
        }
        emp_signup = SignUpForm(bound_values)
        context = {
            'error': error,
            'emp_signup': emp_signup,
        }
    return render(request, 'emp_pro.html', {'emp_signup': context})


def emp_company_post(request):
    all_company = CompanyDetails.objects.all()
    error = ''
    if request.method == "POST":
        emp_comp_det_post = CompanyDetailForm(request.POST)
        context = {
            'emp_comp_det_post': emp_comp_det_post,
            'errors': error,
            'all_company': all_company,
        }
        if emp_comp_det_post.data['company']:
            emp = Employer.objects.get(user=request.user)
            emp.company_details = CompanyDetails.objects.get(company_name=emp_comp_det_post.data['company'])
            emp.save()
            return HttpResponseRedirect(reverse('emp_dash'))
        if emp_comp_det_post.is_valid():
            emp_comp_det_post.save()
            return HttpResponseRedirect(reverse('emp_dash'))
    else:
        emp_comp_det_post = CompanyDetailForm()
    context = {
        'emp_comp_det_post': emp_comp_det_post,
        'errors': error,
        'all_company': all_company,
    }
    return render(request, 'emp_comp_post.html', context)


'''
def job_post_apply(request):
    all_job_posts = JobPost.objects.filter(is_active=True)
    required_job_post = []
    for job_post in all_job_posts:
        job_application = JobApplication.objects.filter(
            student__user=request.user, jobpost=job_post)
        if(len(job_application) == 0):
            required_job_post.append(job_post)
    return render(request, 'emp_job_post.html', {'job_post': required_job_post})



def create_job_post(request):
    obj = JobPost.objects.all()
    return render(request, 'alljobpost.html', {'obj': obj})
'''
