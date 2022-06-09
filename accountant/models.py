from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models

# Create your models here.

class SalaryProject(models.Model):
   emp_id=models.IntegerField()
   comp_id=models.IntegerField()
   sal_id=models.IntegerField()

