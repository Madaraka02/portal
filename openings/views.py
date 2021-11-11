from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')

@login_required
def admin(request):
    if request.user.is_staff:
        
        job_list = Jobs.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(job_list, 15)
        try:
            jobs = paginator.page(page)
        except PageNotAnInteger:
            jobs = paginator.page(1)
        except EmptyPage:
            jobs = paginator.page(paginator.num_pages)

       
        company_list = Company.objects.all().order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(company_list, 15)
        try:
            companies = paginator.page(page)
        except PageNotAnInteger:
            companies = paginator.page(1)
        except EmptyPage:
            companies = paginator.page(paginator.num_pages)

        school_list = School.objects.all().order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(school_list, 15)
        try:
            schools = paginator.page(page)
        except PageNotAnInteger:
            schools = paginator.page(1)
        except EmptyPage:
            schools = paginator.page(paginator.num_pages)

        student_list = Student.objects.all().order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(student_list, 15)
        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)

        context = {
            'companies':companies,
            'jobs':jobs,
            'schools':schools,
            'students':students
        }
        return render(request, 'admin.html', context)
    return redirect('home') 
#  createview displays a form fro creating an object and saves the object else returns none
class company_register(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'companyreg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('portaladmin')

class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'studentreg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('portaladmin')

class SchoolSignUpView(CreateView):
    model = User
    form_class = SchoolSignUpForm
    template_name = 'schoolreg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'school'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('portaladmin')        

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login-student.html')      

def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('companies')
    return render(request, 'login-campany.html')

def school_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('schools')
    return render(request, 'login-school.html')        
def logout_user(request):
    logout(request)
    return redirect('home')


def jobs_details(request, id):

    job = Jobs.objects.filter(id=id)
    context = {
        'job': job
    }
    return render(request, 'jobs-details.html', context)
@login_required 
def delete_job(request, id):
    if request.user.is_staff or request.user.is_company:
        job = Jobs.objects.get(id=id)
        job.delete()
        return redirect('company')  



@login_required 
def updateJob(request, id):
    if request.user.is_staff or request.user.is_company:
        job = Jobs.objects.get(id=id)
        form = JobForm(instance=job)

        if request.method == "POST":
            form = JobForm(request.POST or None, request.FILES, instance=job)

            if form.is_valid():
                
                form.save()
                return redirect('company')
    context ={
        'job': job,
        'form': form

    }
    return render(request, 'company-update-jobs.html', context) 


@login_required 
def delete_company(request, id):
    if request.user.is_staff:
        company = Company.objects.get(id=id)
        company.delete()
        return redirect('portaladmin') 


@login_required 
def updateCompany(request, id):
    if request.user.is_staff or request.user.is_company:
        company = Company.objects.get(id=id)
        form = CompanyForm(instance=company)

        if request.method == "POST":
            form = CompanyForm(request.POST or None, request.FILES, instance=company)

            if form.is_valid():
                
                form.save()
                return redirect('portaladmin')
        context ={
            'company': company,
            'form': form

        }
        return render(request, 'admin-update-companies.html', context)     
@login_required   
def dashboard(request):
    if request.user.is_student or request.user.is_staff:
        jobs = Jobs.objects.all().order_by('-id')
        context = {
            'jobs':jobs,

        }
        return render(request, 'dashboard.html', context)

    return redirect('home')    

@login_required 
def delete_school(request, id):
    if request.user.is_staff:
        school = School.objects.get(id=id)
        school.delete()
        return redirect('portaladmin') 

@login_required 
def updateSchool(request, id):
    if request.user.is_staff or request.user.is_school:
        school = School.objects.get(id=id)
        form = SchoolForm(instance=school)

        if request.method == "POST":
            form = SchoolForm(request.POST or None, request.FILES, instance=school)

            if form.is_valid():
                
                form.save()
                return redirect('portaladmin')
    context ={
        'school': school,
        'form': form

    }
    return render(request, 'admin-update-school.html', context)      

@login_required 
def Studentdel(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('school') 

@login_required 
def updateStudent(request, id):
    if request.user.is_staff or request.user.is_school:
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)

        if request.method == "POST":
            form = StudentForm(request.POST or None, request.FILES, instance=student)

            if form.is_valid():
                
                form.save()
                return redirect('school')
    context ={
        'student': student,
        'form': form

    }
    return render(request, 'school-update-student.html', context) 



def company(request, id):
    company = Company.objects.filter(id=id).first()
    
    job = Jobs.objects.filter(company=company).order_by('-id')
    applications = Application.objects.filter(job__in=job)
    page = request.GET.get('page', 1)
    paginator = Paginator(job, 15)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    
    form = JobForm()

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('company') 
    context = {
        'jobs':jobs,
        'company':company,
        'form':form,
        'applications':applications
    }
    return render(request, 'company.html', context)

def school(request, id):
    school = School.objects.get(id=id)
    student_list = Student.objects.filter(school=school).order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(student_list, 15)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'school':school,
        'students':students,
    }
    return render(request, 'school.html', context)

def all_schools(request):
    schools = School.objects.all().first()
    return render(request, 'schools.html')

def all_companies(request):
    companies = Company.objects.all().first()
    return render(request, 'companies.html')

def apply_job(request):
    form = ApplicationForm()

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    context = {
        'form':form
    }    
    return render(request, 'apply.html', context)