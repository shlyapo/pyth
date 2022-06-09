from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
from django.urls import reverse
#from employee.models import Salary
#from manager.models import Storage



class User(AbstractUser):
   # name = models.CharField(max_length=30, verbose_name='name', unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    passport_numer = models.CharField(max_length=20, verbose_name='Passport number')
    passport_series = models.CharField(max_length=20, verbose_name='Passport series')
    age = models.PositiveIntegerField(default=18, verbose_name='Age')


        # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    #def __str__(self):
       # return self.user.username


class Company(models.Model):
    name=models.CharField(max_length=30, unique=True)
    #Storage.objects.create()


class Employee(models.Model):
    companies=models.ManyToManyField(Company)
    #salaries=models.ForeignKey(Salary, on_delete=models.CASCADE)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    date_salary=models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ["-date_salary"]

    def __str__(self):
        return self.user.username


#class SalaryList(models.Model):
 #   profession = models.CharField(max_length=100, verbose_name='Salary')
  #  sum = models.PositiveIntegerField(default=0, verbose_name='Sum')
   # company_id = models.IntegerField(default=0)
    #employee_id = models.IntegerField(default=0)
    #date_salary = models.DateTimeField(auto_now_add=True)
    #is_now = models.BooleanField(default=False)

    #class Meta:
     #   ordering = ["-date_salary"]

    #def __str__(self):
    #    return self.user.username


class Salary(models.Model):
    profession=models.CharField(max_length=100, verbose_name='Salary')
    #salary_list=models.ForeignKey(SalaryList, on_delete=models.CASCADE)
    sum=models.PositiveIntegerField(default=0, verbose_name='Sum')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, unique=False)
    date_salary = models.DateTimeField(auto_now_add=True)
    is_now=models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_salary"]

    def __str__(self):
        return self.user.username




class Manager(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Accountant(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




#user = User.objects.create_user('myusername',
                                #'myemail@mail.com','mypassword')

#user.first_name='John'
#user.last_name='Citizen'
#user.save()