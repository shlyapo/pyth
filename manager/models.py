from django.db import models

# Create your models here.
from first.models import Company


class EmployeeProject(models.Model):
   comp_id=models.IntegerField()
   emp_id=models.IntegerField()

class Storage(models.Model):
   comp_id=models.IntegerField(default=0)
   sum=models.PositiveIntegerField(default=0)


class TransMoney(models.Model):
   company=models.ForeignKey(Company, on_delete=models.CASCADE)
   sum=models.PositiveIntegerField(default=0)
   date_of_trans=models.DateTimeField(auto_now_add=True)
   status = models.CharField(default="add money", max_length=300)




