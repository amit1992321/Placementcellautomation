from django.contrib import admin
from django.urls import path
from StudentPanel import views as StudentPanelView
# Change 2 Do this kind of approach in other places
from EmployerPanel import views as EmployerPanelView
from TpoPanel import views as TpoPanelView
from placement import views
from django.conf.urls.static import static
from django.conf import settings
from JobApplication import views as JobApplicationView


urlpatterns = [
    path('', views.homepage, name="home_page"),
    path('tpologin/', admin.site.urls),
    # Login For all Dashboard Separately

    path('signin/', views.signin, name="signin"),
    path('developer/', views.developer, name="developer"),
    path('contact/', views.contact_us, name="contact_us"),
    path('logout/', views.logout, name="logout"),

    # Student views
    path('stu-dashboard/', StudentPanelView.stu_dashboard, name="stu_dash"),
    path('stu-profile/', StudentPanelView.stu_profile, name="stu_profile"),
    path('stu-register-per/', StudentPanelView.stu_register_per, name="stu_regper"),
    path('stu-register-edu/', StudentPanelView.stu_register_edu, name="stu_regedu"),
    path('stu-register-pro/', StudentPanelView.stu_register_pro, name="stu_regpro"),
    path('stu-signup/', StudentPanelView.student_signup, name="stu_signup"),
    path('stu-job-apply/', StudentPanelView.stu_job_apply, name="stu_job_apply"),
    path('stu-verify/', StudentPanelView.student_verify, name="stu_verify"),
    path('application-status/', StudentPanelView.application_status,
         name="application_status"),

    # Employee (menu)
    path('emp-signup/', EmployerPanelView.employer_signup, name="emp_signup"),
    path('emp-dashboard/', EmployerPanelView.emp_dashboard, name="emp_dash"),
    path('emp-profile/', EmployerPanelView.emp_profile, name="emp_profile"),
    path('emp-stu-list/', EmployerPanelView.emp_stu_list, name="emp_stu_list"),
    path('emp-new-jobpost/', EmployerPanelView.emp_newjobpost, name="emp_newjobpost"),
    path('emp-create-pro/', EmployerPanelView.emp_create_pro, name="emp_create_pro"),
    path('emp-app-review/', EmployerPanelView.stu_app_review, name="stu_app_review"),
    path('emp-stu-app/', EmployerPanelView.stu_app, name="stu_app"),
    path('emp-job-post/', EmployerPanelView.job_post, name="job_post"),
    path('emp-comp-edit/', EmployerPanelView.emp_company_details,
         name="edit_comp_details"),
    path('emp-company-details/',
         EmployerPanelView.emp_company_post, name='emp_comp_post'),
    # Employee (Content)
    path('emp-register', EmployerPanelView.emp_reg_info, name="emp_profile_edit"),
    # path('emp-jobpost', EmployerPanelView.emp_jobpost, name="emp_job"),
    path('job-post-apply/<int:job_post_id>/', JobApplicationView.job_post_apply, name="job_post_apply"),
    # path('create-job-post/', EmployerPanelView.create_job_post, name="create_job_post"),
    # path('job-post-list/', EmployerPanelView.job_list, name='job_post_list'),
    path('post-job-apply-submit/', JobApplicationView.post_job_apply, name="post_job_apply_submit"),


    # Tpo Menu
    path('tpo-dashboard/', TpoPanelView.tpo_dashboard, name="tpo_dash"),
    path('tpo-profile/', TpoPanelView.tpo_profile, name="tpo_profile"),
    path('tpo-stu-list/', TpoPanelView.tpo_student_list, name='stu_list'),
    path('tpo-emp-list/', TpoPanelView.tpo_employer_list, name='emp_list'),
    path('tpo-job-list/', TpoPanelView.tpo_job_post_list, name='tpo_job_post_list'),


    # TPO Content
    path('tpo-register', TpoPanelView.tpo_register, name="tpo_reg"),
    path('tpo-signup/', TpoPanelView.tpo_signup, name="tpo_signup"),


    # path('logout', )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''path('stu-signin/', StudentPanelView.student_signin, name="stu_signin"),
                path('emp-signin/', employer_signin, name="emp_signin"),
                path('tpo-signin/', tpo_signin, name="tpo_signin"),
                # Registration Page
            '''
