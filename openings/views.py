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
        job_count = Jobs.objects.all().count()
        school_count = School.objects.all().count()
        student_count = Student.objects.all().count()
        company_count = Company.objects.all().count()

        context = {
            'job_count':job_count,
            'company_count':company_count,
            'student_count':student_count,
            'school_count':school_count,
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
        # login(self.request, user)
        messages.success(self.request, "Company added successfully")
        return redirect('company_register')
        
class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'studentreg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
            # login(self.request, user)
        messages.success(self.request, "Student added successfully")
        return redirect('student_register')

class SchoolSignUpView(CreateView):
    model = User
    form_class = SchoolSignUpForm
    template_name = 'schoolreg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'school'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        messages.success(self.request, "school added successfully")
        return redirect('school_register')        

def site_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_school:
                return redirect('school', id=user.school.id)
            elif request.user.is_company:
                return redirect('company', id=user.company.id)  
            elif request.user.is_student:
                return redirect('dashboard')
            elif request.user.is_staff:
                return redirect('portaladmin')
            else:
                return redirect('home')              
    return render(request, 'login.html')  

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
        messages.success(request, "Job was deleted successfully")
        return redirect('company', id=request.user.company.id) 


@login_required 
def updateJob(request, id):
    if request.user.is_staff or request.user.is_company:
        job = Jobs.objects.get(id=id)
        form = JobForm(instance=job)

        if request.method == "POST":
            form = JobForm(request.POST or None, request.FILES, instance=job)

            if form.is_valid():
                avail = form.save(commit=False)
                avail.company = request.user.company
                avail.save()
                messages.success(request, "Job was updated successfully")
                return redirect('company', id=request.user.company.id)
    context ={
        'job': job,
        'form': form

    }
    return render(request, 'company-update-jobs.html', context) 


@login_required 
def delete_company(request, pk):
    if request.user.is_staff:
        company = Company.objects.get(id=pk)
        company.delete()
        messages.success(request, "Company was deleted successfully")
        return redirect('admin_companies') 


@login_required 
def updateCompany(request, id):
    if request.user.is_staff or request.user.is_company:
        company = Company.objects.get(id=id)
        form = CompanyForm(instance=company)

        if request.method == "POST":
            form = CompanyForm(request.POST or None, request.FILES, instance=company)

            if form.is_valid():
                
                avail = form.save(commit=False)
                avail.company = company
                avail.save()
                messages.success(request, "Company was updated successfully")
                return redirect('admin_companies')
        context ={
            'company': company,
            'form': form

        }
        return render(request, 'admin-update-companies.html', context)     
@login_required   
def dashboard(request):
    if request.user.is_student or request.user.is_staff:
        jobs = Jobs.objects.all().order_by('-id')
        paginator = Paginator(jobs, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        
        context = {
            'page_obj': page_obj,

        }
        return render(request, 'dashboard.html', context)

    return redirect('home')    

@login_required 
def delete_school(request, pk):
    if request.user.is_staff:
        school = School.objects.get(id=pk)
        school.delete()
        messages.success(request, "School was deleted successfully")
        return redirect('admin_schools') 

@login_required 
def updateSchool(request, id):
    if request.user.is_staff or request.user.is_school:
        school = School.objects.get(id=id)
        form = SchoolForm(instance=school)

        if request.method == "POST":
            form = SchoolForm(request.POST or None, request.FILES, instance=school)

            if form.is_valid():
                avail = form.save(commit=False)
                avail.school = school
                avail.save()
                messages.success(request, "School was updated successfully")
                return redirect('admin_schools')
    context ={
        'school': school,
        'form': form

    }
    return render(request, 'admin-update-school.html', context)      
 
@login_required     
def delete_student(request, pk):
    if request.user.is_staff or request.user.is_school:
        student = Student.objects.get(id=pk)
        student.delete()
        messages.success(request, "Student was deleted successfully")
        return redirect('school', id=request.user.school.id) 

@login_required 
def updateStudent(request, id):
    if request.user.is_staff or request.user.is_school:
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)

        if request.method == "POST":
            form = StudentForm(request.POST or None, request.FILES, instance=student)

            if form.is_valid():
                avail = form.save(commit=False)
                avail.student = student
                avail.save()
                messages.success(request, "Student was successfully Updated")
                return redirect('school', id=request.user.school.id) 
    context ={
        'student': student,
        'form': form

    }
    return render(request, 'school-update-student.html', context) 


@login_required
def company(request, id):
    company = Company.objects.filter(id=request.user.company.id).first()
    
    job = Jobs.objects.filter(company=company).order_by('-id')
    applications = Application.objects.filter(company_id=request.user.company.id).order_by('-id')
    #paginate applications
        
    paginator = Paginator(applications, 4)
    page_number = request.GET.get('page')
    application_obj = paginator.get_page(page_number) 
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
            avail = form.save(commit=False)
            avail.company = request.user.company
            avail.save()
            
        return redirect('company', id=request.user.company.id) 
    context = {
        'jobs':jobs,
        'company':company,
        'form':form,
        'application_obj':application_obj
    }
    return render(request, 'company.html', context)
@login_required
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

    form = StudentSignUpForm()

    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            avail = form.save(commit=False)
            avail.school = request.user.school
            avail.save()
    context = {
        'school':school,
        'students':students,
        'form':form
    }
    return render(request, 'school.html', context)


def jobs_details(request, id):
    if request.user.is_student:
        jobs = Jobs.objects.filter(id=id)
        job = get_object_or_404(Jobs, id=id)
        company = job.company
        student = request.user.student
        form = ApplicationForm()
        
        if request.method == "POST":
            form = ApplicationForm(request.POST)
            if form.is_valid():
                appl_form = form.save(commit=False)
                appl_form.student = request.user.student
                appl_form.job = job
                appl_form.company = company
                appl_form.save()
                messages.success(request, "application was successful")
                return redirect('dashboard') 
    context = {
        'jobs':jobs,
        'form':form
    }
    return render(request, 'job-details.html', context)

 
@login_required 
def delete_application(request, id):
    if request.user.is_company:
        application = Application.objects.get(id=id)
        application.delete()
        messages.success(request, "application was deleted successfully")
        return redirect('company', id=request.user.company.id)  

@login_required 
def admin_schools(request):
    if request.user.is_staff:
        school_list = School.objects.all().order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(school_list, 15)
        try:
            schools = paginator.page(page)
        except PageNotAnInteger:
            schools = paginator.page(1)
        except EmptyPage:
            schools = paginator.page(paginator.num_pages)
        context = {
            'schools':schools,
        }    
    return render(request, 'admin-schools.html', context) 

@login_required 
def admin_students(request):
    if request.user.is_staff:
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
            'students':students,
        } 
    return render(request, 'admin-students.html', context) 

@login_required 
def admin_companies(request):
    if request.user.is_staff:
        company_list = Company.objects.all().order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(company_list, 15)
        try:
            companies = paginator.page(page)
        except PageNotAnInteger:
            companies = paginator.page(1)
        except EmptyPage:
            companies = paginator.page(paginator.num_pages)
        context = {
            'companies':companies
        } 
        return render(request, 'admin-company.html', context)   

@login_required 
def admin_jobs(request):
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

        context = {
            'jobs':jobs
        }  
        return render(request, 'admin-jobs.html', context)     

        