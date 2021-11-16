from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    official_name = models.CharField(max_length=100, null=True, default="school")
    email = models.CharField(max_length=100, null=True)

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=100, null=True, unique=True) 
    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True) 
    course = models.CharField(max_length=100, null=True ) 
    transcript = models.FileField(upload_to='transcripts/',null=True)

    def __str__(self):
        return self.user.username

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.user.username

class Jobs(models.Model):
    title = models.CharField(max_length=1000)
    required_skills = RichTextField()
    is_open = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="Null",null=True)
    description = RichTextField(null=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.job.title