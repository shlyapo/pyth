from django.db import models

# Create your models here.
#from first.models import Company, Employee, User



class Money(models.Model):
    employee_id=models.IntegerField(default=0)
    sum=models.PositiveIntegerField(default=0)
