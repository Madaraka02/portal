from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=100, null=True) 
    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True) 
    course = models.CharField(max_length=100, null=True ) 

    def __str__(self):
        return self.user.username

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=100) 

    def __str__(self):
        return self.user.username

class Jobs(models.Model):
    title = models.CharField(max_length=1000)
    required_skills = RichTextField()
    is_open = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="Null",null=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.job.title