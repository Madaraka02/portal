from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from .models import *



class SchoolSignUpForm(UserCreationForm):
    official_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    reg_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.official_name = self.cleaned_data["official_name"]
        user.email = self.cleaned_data["email"]
        user.is_school = True
        user.save()
        school = School.objects.create(user=user)
        school.reg_no = self.cleaned_data.get('reg_no')
        school.save()
        return user

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label="Please choose a School")
    course = forms.CharField(required=True)
    # transcript = forms.FileField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.school = self.cleaned_data.get('school')
        student.course = self.cleaned_data.get('course')
        # student.transcript = self.cleaned_data.get('transcript')
        student.save()
        return user

class CompanySignUpForm(UserCreationForm):
    official_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    reg_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.official_name = self.cleaned_data["official_name"]
        user.email = self.cleaned_data["email"]
        user.is_company = True
        user.save()
        company = Company.objects.create(user=user)
        company.reg_no = self.cleaned_data.get('reg_no')
        company.save()
        return user    


class JobForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ('title', 'required_skills', 'is_open', 'description')       


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'                

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'                        

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ( )        
        