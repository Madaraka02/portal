from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from .models import *



class SchoolSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_school = True
        user.save()
        school = School.objects.create(user=user)
        return user

class StudentSignUpForm(UserCreationForm):
    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label="Please choose a School")
    course = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.school = self.cleaned_data.get('school')
        student.course = self.cleaned_data.get('course')
        
        return user

class CompanySignUpForm(UserCreationForm):
    reg_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = Company.objects.create(user=user)
        company.reg_no = self.cleaned_data.get('reg_no')
        return user    


class JobForm(ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'        


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
        fields = '__all__'         