from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('portaladmin/', admin, name="portaladmin"),
    path('company/register/', company_register.as_view(), name="company_register"),
    path('student/register/', student_register.as_view(), name="student_register"),
    path('school/register/', SchoolSignUpView.as_view(), name="school_register"),
    path('login/',  site_login, name="site_login"),
    path('logout/',  logout_user, name="logout"),
    path('student/dashboard/',  dashboard, name="dashboard"),

    path('delete/job/<int:id>/',  delete_job, name="delete_job"),
    path('update/job/<int:id>/',  updateJob, name="update_job"),

    path('update/company/<int:id>/',  updateCompany, name="update_company"),

    path('update/school/<int:id>/',  updateSchool, name="update_school"),

    path('update/student/<int:id>/',  updateStudent, name="update_student"),

    path('student/certs/',  studentacc, name="studentacc"),
    path('companies/<str:id>/',  company, name="company"),
    path('schools/<str:id>/',  school, name="school"),
    path('details/job/<int:id>/', jobs_details, name="job_details"),
    path('delete/application/<int:id>/',  delete_application, name="delete_application"),

    path('search/', search, name='search'),
    path('search/courses/', searchStudentByCourse, name='searchcourses'),

    path('portaladmin/schools/',  admin_schools, name="admin_schools"),
    path('portaladmin/students/',  admin_students, name="admin_students"),
    path('portaladmin/companies/', admin_companies, name="admin_companies"),
    path('portaladmin/jobs/',  admin_jobs, name="admin_jobs"),
    url(r'^delete_student/(?P<pk>[0-9]+)/$', delete_student,name="delete"),
    url(r'^delete_company/(?P<pk>[0-9]+)/$', delete_company,name="deletecom"),
    url(r'^delete_school/(?P<pk>[0-9]+)/$', delete_school,name="deleteshc"),
    
# password reset

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
    name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
    name="password_reset_confirm"),
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
     name="password_reset_complete"),

]