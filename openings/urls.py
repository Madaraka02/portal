from django.urls import path
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

    path('delete/company/<int:id>/',   delete_company, name=" delete_company"),
    path('update/company/<int:id>/',  updateCompany, name="update_company"),

    path('delete/school/<int:id>/',   delete_school, name=" delete_school"),
    path('update/school/<int:id>/',  updateSchool, name="update_school"),

    path('delete/student/<int:id>/',   delete_student, name=" delete_student"),
    path('update/student/<int:id>/',  updateStudent, name="update_student"),
    
    path('companies/<str:id>/',  company, name="company"),
    path('schools/<str:id>/',  school, name="school"),
    path('applicatons/',  apply_job, name="apply"),
    
]