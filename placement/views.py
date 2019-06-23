from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from placement.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login


def contact_us(request):
    return render(request, 'contactus.html', {})


def developer(request):
    return render(request, 'developer.html', {})


def homepage(request):
    return render(request, "home.html", {})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home_page'))


def signin(request):
    error = ''
    if request.user.is_authenticated:
        if "employer" in [i.name for i in request.user.groups.all()]:
            return HttpResponseRedirect(reverse('emp_dash'))
        if "Student" in [i.name for i in request.user.groups.all()]:
            return HttpResponseRedirect(reverse('stu_dash'))
        if "tpo_group" in [i.name for i in request.user.groups.all()]:
            return HttpResponseRedirect(reverse('tpo_dash'))
        else:
            return HttpResponseRedirect(reverse('home_page'))
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            context = {
                'login_form': login_form,
                'error': error
            }
            if login_form.is_valid():
                usernames = login_form.cleaned_data['username']
                passwords = login_form.cleaned_data['password']
                user = authenticate(
                    request, username=usernames, password=passwords)
                if user is not None:
                    django_login(request, user)
                    if "employer" in [i.name for i in request.user.groups.all()]:
                        return HttpResponseRedirect(reverse('emp_dash'))
                    if "Student" in [i.name for i in request.user.groups.all()]:
                        return HttpResponseRedirect(reverse('stu_dash'))
                    if "tpo_group" in [i.name for i in request.user.groups.all()]:
                        return HttpResponseRedirect(reverse('tpo_dash'))
                else:
                    error = "User and name password are incorrect"
        else:
            login_form = LoginForm()
        context = {
            'login_form': login_form,
            'error': error,
        }
    return render(request, "signin.html", context)
