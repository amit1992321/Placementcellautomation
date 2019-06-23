from django.shortcuts import render
from StudentPanel.forms import SignUpForm, Stu_Form_per
from StudentPanel.forms import Stu_Form_edu, Stu_Form_pro
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, Group
from StudentPanel.models import StudentPersonalDetail, StudentEducationalQualifications, StudentJobApplicationDetail
from EmployerPanel.models import JobPost
from JobApplication.models import JobApplication
# Create your views here.


def student_signup(request):

    error = ""
    if request.user.is_authenticated:

        if "Student" in [i.name for i in request.user.groups.all()]:

            return HttpResponseRedirect(reverse('stu_dash'))
        else:

            return HttpResponseRedirect(reverse('stu_signin'))
    else:
        if request.method == 'POST':

            stu_reg_form = SignUpForm(request.POST)

            if stu_reg_form.is_valid():

                username = stu_reg_form.cleaned_data['username']
                # password = emp_reg.cleaned_data['TPO_Password']
                # Create new user
                u = User.objects.create(
                    username=username,
                    first_name=stu_reg_form.cleaned_data['first_name'],
                    last_name=stu_reg_form.cleaned_data['last_name'],
                    email=stu_reg_form.cleaned_data['email'],
                    is_active=True)
                u.set_password(stu_reg_form.cleaned_data['password'])

                my_group = Group.objects.get(name='Student')
                my_group.user_set.add(u)

                u.save()

                return HttpResponseRedirect('/signin/')
            else:

                return HttpResponseRedirect(reverse('stu_signup'))

        else:

            stu_reg_form = SignUpForm()
            context = {
                'stu_reg_form': stu_reg_form,
                'error': error

            }
    return render(request, "student_signup.html", context)


def stu_register_per(request):
    current_user = request.user
    obj = StudentPersonalDetail.objects.filter(user=current_user)
    print(obj)
    object = obj.last()
    print(object)
    if request.method == 'POST':
        print('6')
        stu_reg_per = Stu_Form_per(request.POST)
        print('7')
        if stu_reg_per.is_valid():
            print('8')
            stu_reg_per.save()
            print('9')
            return HttpResponseRedirect(reverse('stu_dash'))
        import ipdb; ipdb.set_trace()
    else:
        print('10')
        stu_reg_per = Stu_Form_per()
    return render(request, 'stu_register_per.html', {'stu_reg_per': stu_reg_per, 'obj': object})


def stu_register_edu(request):
    current_user = request.user
    obj = StudentEducationalQualifications.objects.filter(studentpersonaldetail__user=current_user)
    objects = obj.last()
    if request.method == 'POST':
        stu_reg_edu = Stu_Form_edu(request.POST)
        if stu_reg_edu.is_valid():
            stu_reg_edu.save()
            return HttpResponseRedirect(reverse('stu_dash'))
    else:
        stu_reg_edu = Stu_Form_edu()
    return render(request, 'stu_register_edu.html', {'stu_reg_edu': stu_reg_edu, 'obj': objects})


def stu_register_pro(request):
    current_user = request.user
    obj = StudentJobApplicationDetail .objects.filter(studentpersonaldetail__user=current_user)
    objects = obj.last()
    if request.method == 'POST':
        stu_reg_pro = Stu_Form_pro(request.POST)
        if stu_reg_pro.is_valid():
            stu_reg_pro.save()
            return HttpResponseRedirect(reverse('stu_dash'))
    else:
        stu_reg_pro = Stu_Form_pro()
    return render(request, 'stu_register_pro.html', {'stu_reg_pro': stu_reg_pro, 'obj': objects})


def stu_dashboard(request):
    current_user = request.user
    obj = StudentPersonalDetail.objects.filter(user=current_user)
    object = obj.last()
    obj1 = obj.last().uid
    edu_obj = StudentEducationalQualifications.objects.filter(studentpersonaldetail__user=current_user)
    edu_objects = edu_obj.last()
    return render(request, "stu_dashboard.html", {'obj': object, 'edu_objects': edu_objects})


def stu_profile(request):
    return render(request, "stu_profile.html", {})


def stu_job_apply(request):
    all_job_posts = JobPost.objects.filter(is_active=True)
    required_job_post = []
    for job_post in all_job_posts:
        job_application = JobApplication.objects.filter(
            student__user=request.user, jobpost=job_post)
        if(len(job_application) == 0):
            required_job_post.append(job_post)
    return render(request, 'stu_job_apply.html', {'job_post': required_job_post})


def student_verify(request):
    obj = StudentPersonalDetail.objects.all()
    return render(request, 'stu_varify.html', {'obj': obj})


def application_status(request):
    obj = JobApplication.objects.filter(application_status='Inprocess')
    required_job_post = []
    for job_post in obj:
        job_application = JobApplication.objects.filter(
            employer__user=request.user, jobpost=job_post)
        if(len(job_application) == 0):
            required_job_post.append(job_post)
    return render(request, 'stu_varify.html', {'obj': obj})
